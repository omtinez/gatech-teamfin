from FHIR import FHIR
from FitbitAPI import FitbitAPI
import sqlite3


def sync_with_fhir(users):
    fbapi = FitbitAPI()
    fhir = FHIR('http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base')
    db = sqlite3.connect('../database/jogrx.db')
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
                fhir.send_exercise_obs(diff_steps, fhir_id)
                print "New steps saved"
        db.commit()
        c.close()
