from bottle import route, view, request, response, template
from datetime import datetime
import sqlite3
from permissions import permissions
import requests, json

def create_patient(url,patient):
    # EC 112115 Expects patient dictionary and HISP address
    # returns response to parse out id
    query = 'base/Patient/'
    base_url = url + query
    # create the payload using example
    payload = {"active": 'true',
        "address": [{"city": "",
        "line": [""],
        "postalCode": "",
        "state": "",
        "use": ""}],
        "birthDate": "",
        "gender": "",
        "id": "",
        "name": [{"family": [""], "given": [""]}],
        "resourceType": "",
        "text": {"status": ""}}

    payload["name"][0]["family"] = patient['lname']
    payload["name"][0]["given"] = patient['fname']
    payload["birthDate"] = patient['dob']
    payload["active"] = 'true'
    payload["resourceType"] = "Patient"
    payload["text"] = {"status": "generated"}
    payload["id"] = '1'
    payload["gender"] = patient['sex']
    payload["address"][0]["city"] = patient['city']
    payload["address"][0]["line"][0] = patient['street']
    payload["address"][0]["postalCode"] = patient['postal']
    payload["address"][0]["state"] = patient['state']
    payload["address"][0]["use"] = "home"        

    headers = {'content-type': 'application/json+fhir'}

    r = requests.post(base_url, data=json.dumps(payload), headers=headers)

    # if r.status_code != 201:
    #     return r.text
    # else:
    #     return r.status_code
    return r

@route('/doctors_HISP')
@view('doctors_HISP')
def doctors_HISP():
    return dict(
        title='Connect with your doctor',
        message='',
        year=datetime.now().year
    )

@route('/doctors_HISP', method='POST')
@view('doctors_HISP')
def do_doctors_HISP():

    server              = request.forms.get('hispAddress').strip()
    patient             = {}
    patient['fname']    = request.forms.get('firstname').strip() 
    patient['lname']    = request.forms.get('lastname').strip()
    patient['dob']      = request.forms.get('birthdate').strip()
    patient['street']   = request.forms.get('street').strip()
    patient['postal']   = request.forms.get('postal').strip()
    patient['city']     = request.forms.get('city').strip()
    patient['state']    = request.forms.get('state').strip()
    patient['sex']      = request.forms.get('sex').strip()

    # EC 1121 ensure all required fields before proceeding
    # query the server for the patient id using family/given name and dob
    url = server + "/base/Patient?birthdate=>%s"%patient['dob'] 
    url += "&family=%s"%patient['lname']
    url += "&given=%s"%patient['fname']   

    headers = {'content-type': 'application/json+fhir'}

    r = requests.get(url, headers=headers)

    r_dict = r.json()
    if r_dict['total'] == 1:
        entry = r_dict['entry']
        resource = entry[0]['resource']
        hisp_id = resource['id']

    else:
        # send a dict with patient details
        r = create_patient(url,patient)
        # if we create, then get the id from the headers attribute
        # return template('<h2>Hello {{name}}, Please consult with your HISP provider BUT we created an account for you since none was found</h2>', name=patient['fname'])

    l_index = r.headers['Content-Location'].index('Patient/') + 8
    hisp_id = r.headers['Content-Location'][l_index:]
    userid = request.get_cookie("userid", secret='teamfin')
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    # EC update HISP ID
    c.execute("UPDATE user SET server=?, hisp_id=? WHERE id=?", (server, hisp_id, int(userid)))
    db.commit()
    c.close()

    return permissions()
