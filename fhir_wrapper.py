import requests
import json

base_url = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base/Observation"

payload = {
    'resourceType': 'Observation',
    'code': {
        'coding': [
            {
                'system': 'http://lonic.org',
                'code': '8302-2',
                'display': 'Body height'
            }
        ]
    },
    'valueQuantity': {
        'value': 160.0,
        'units': 'cm',
        'system': 'http://unitsofmeasure.org',
        'code': 'cm'
    },
    'appliesDateTime': '2015-06-30T19:45:00-04:00',
    'status': 'final',
    'reliability': 'ok',
    'subject': {
        'reference': 'Patient/1'
    },
    'encounter': {
        'reference': '1'
    }
}

headers = {'content-type': 'application/json+fhir'}
r = requests.post(base_url, data=json.dumps(payload), headers=headers)
if r.status_code != 201:
    print r.text
    print "Error"
else:
    print "Encounter sent successfully"
