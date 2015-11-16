import requests
import json
from time import gmtime, strftime

# base_url = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base/Observation"


# Expects the minutes the user exercised and a user object with attribute id
# that cooresponds to the patients fhir id
class FHIR:
    def __init__(self, url):
        self.base_url = url

    def send_exercise_obs(steps, userid):
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
        r = requests.post(self.base_url, data=json.dumps(payload), headers=headers)
        if r.status_code != 201:
            return r.text
        else:
            return r.status_code
