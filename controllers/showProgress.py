from bottle import route, view, request, response, template
from datetime import datetime
import sqlite3
from DBAPI import *


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
def displayData(input):
    return dict(stepsTaken=input,year=datetime.datetime.now().year)