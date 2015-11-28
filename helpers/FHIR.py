import requests
import json
import re
from time import gmtime, strftime

# base_url = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base/Observation?_format=json"


# Expects the minutes the user exercised and a user object with attribute id
# that cooresponds to the patients fhir id
class FHIR:
    def __init__(self, url):
        self.base_url = url

    def send_exercise_obs(self, steps, userid):
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
                'units': 'steps',
                'system': 'http://unitsofmeasure.org',
                'code': 'steps'
            },
            'appliesDateTime':  strftime("%Y-%m-%dT%H:%M:%S-04:00", gmtime()),
            'status': 'final',
            'reliability': 'ok',
            'subject': {
                'reference': 'Patient/%s' % userid
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

    # creates a new FHIR patient and returns a patient id
    def create_new_patient(self, user, userid):
        first_name = user[7]
        last_name = user[8]
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
            "gender": "male",
            "birthDate": "1960-05-20",
            "address": [
                {
                    "use": "home",
                    "line": [
                        "370 Zermatt Avenue"
                    ],
                    "city":"Atlanta",
                    "state":"GA",
                    "postalCode":"30308"
                    }
                ],
            "active": 'true'
            }

        headers = {'content-type': 'application/json+fhir'}
        print json.dumps(payload)
        # patient_url = self.base_url + "/Patient/?_format=json"
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
