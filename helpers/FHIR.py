import requests
import json
import re
from time import gmtime, strftime
from FitbitAPI import FitbitAPI
import sqlite3

# Expects the minutes the user exercised and a user object with attribute id
# that cooresponds to the patients fhir id


class FHIR:
    def __init__(self, url):
        self.base_url = url

    def send_exercise_obs(self, steps, fhir_id):
        payload = {
            'resourceType': 'Observation',
            'code': {
                'coding': [
                    {
                        'system': 'http://lonic.org',
                        'code': '41950-7',
                        'display': 'Number of steps in 24 hour Measured'
                    }
                ]
            },
            'valueQuantity': {
                'value': steps,
                'units': 'cm',
                'system': 'http://unitsofmeasure.org',
                'code': 'cm'
            },
            'appliesDateTime':  strftime("%Y-%m-%dT%H:%M:%S-04:00", gmtime()),
            'status': 'final',
            'reliability': 'ok',
            'subject': {
                'reference': 'Patient/%s' % fhir_id
            }
        }

        headers = {'content-type': 'application/json+fhir'}
        print json.dumps(payload)
        obs_url = self.base_url + "/Observation/?_format=json"
        r = requests.post(obs_url, data=json.dumps(payload), headers=headers)
        if r.status_code == 201:
            print "Success"
            print r.headers
            print r.text
            return
        else:
            print "Error"
            print r.headers
            print r.text
            return

    def get_observations(self, fhir_id):
        headers = {'content-type': 'application/json+fhir'}
        obs_url = self.base_url + "/Observation?patient._id=811&_format=json"
        print obs_url
        r = requests.get(obs_url, headers=headers)
        if r.status_code == 200:
            print "Success"
            return r.text
        else:
            print "Error"
            return r.text

    # creates a new FHIR patient and returns a patient id
    def create_new_patient(self, user):
        first_name = user['first_name']
        last_name = user['last_name']
        gender = user['gender']
        birthdate = user['birthdate']

        print "Creating a new patient"
        payload = {
            "resourceType": "Patient",
            "name": [
                {
                    "family": [
                        last_name
                    ],
                    "given":[
                        first_name
                    ]
                }
            ],
            "gender": gender,
            "birthDate": birthdate,
            "address": [
                {
                    "use": "home",
                    "line": [
                        ""
                    ],
                    "city":"",
                    "state":"",
                    "postalCode":""
                    }
                ],
            "active": 'true'
            }

        headers = {'content-type': 'application/json+fhir'}
        print json.dumps(payload)
        patient_url = self.base_url + "/Patient?_format=json"
        r = requests.post(patient_url, data=json.dumps(payload), headers=headers)
        if r.status_code == 201:
            print "Success"
            print r.headers
            print r.json
            patient_id = re.search('Patient/([0-9]+)', r.headers['location']).group(1)
            print "Patient ID: %s" % patient_id
            return patient_id
            # return r.json
        else:
            print "Error"
            print r.headers
            print r.json
            # return r.json
            return None

    def sync_with_fhir(self):
        fbapi = FitbitAPI()
        db = sqlite3.connect('database/jogrx.db')
        c = db.cursor()
        c.execute("SELECT * FROM user")
        users = c.fetchall()
        print users
        for user in users:
            print "-----------"
            print user
            user_id = user[0]
            fitbit_id = user[3]
            fhir_id = user[11]
            current_steps = user[4]
            fitbit_stats = fbapi.pull(str(fitbit_id))
            if fitbit_id is not None and fhir_id is not None:
                if fitbit_stats['Steps'] > current_steps:
                    print "Steps different"
                    c.execute("UPDATE user SET current_steps=? WHERE id=?", (
                        fitbit_stats['Steps'], int(user_id)))
                    diff_steps = fitbit_stats['Steps'] - current_steps
                    self.send_exercise_obs(diff_steps, fhir_id)
                    print "New steps saved"
            db.commit()
            c.close()
