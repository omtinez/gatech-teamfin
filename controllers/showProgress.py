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
    c.execute("SELECT stepsTaken FROM steps WHERE username=='%s'" %(fitbitUsername))
    result = c.fetchone()
    c.close()
    #output = template('displayData',rows=result)
    return displayData(result[0])


@route('/displayData')
@view('displayData')
def displayData():
    fhir = FHIR('http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base')
    observations = fhir.get_observations(22)
    return dict(observations_raw=observations, year=datetime.datetime.now().year)
