from bottle import route, view, request, response, template
from datetime import datetime
import sqlite3
from DBAPI import *
from helpers import FHIR


@route('/showProgress')
@view('showProgress')
def showProgress(fitbitUsername):
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("SELECT * FROM steps WHERE username=?" ,(fitbitUsername,))
    result = c.fetchone()
    c.close()
    #output = template('displayData',rows=result)
    return result[3]

def getFhirID(fitbitID):
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("Select * from user where fitbit_id = ? ", (fitbitID,))
    result = c.fetchone()
    c.close()
    return result[11]

@route('/displayData')
@view('displayData')
def displayData(fitbitID):
    fhir = FHIR('http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base')
    fhir.send_exercise_obs(showProgress(fitbitID), getFhirID(fitbitID))
    observations = fhir.get_observations(getFhirID(fitbitID))
    observationList = observations.split('\n')

    return dict(observations_raw=observations, year=datetime.datetime.now().year)



def progress(currentSteps):
    if (currentSteps<40): return "danger"
    elif(currentSteps<80): return  "warning"
    elif (currentSteps<100): return "info"
    else : return "success"

@route('/displayData', method="POST")
@view('displayCurrentProgress')
def displayCurrentPogress():
    accept = request.forms.get('Accept')
    userid = request.get_cookie("userid", secret='teamfin')
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    if accept:
        c.execute("Select fitbit_id from user WHERE id=?", (int(userid),))
        db.commit()
        tempReslut = c.fetchone()
        c.close()
        currentSteps =showProgress(tempReslut[0])
        precipitation = 10000
        percentage = currentSteps/precipitation * 100
        return dict(stepsTaken=currentSteps,percentage= percentage, progress = progress(percentage), year=datetime.datetime.now().year)
