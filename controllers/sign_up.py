from bottle import route, view, request, response
from datetime import datetime
import sqlite3
import bcrypt
from helpers import FHIR
from fitBitConnect import fitBitConnect

@route('/sign_up', method='GET')
@view('sign_up')
def get_sign_up():
    return dict(year=datetime.now().year)

@route('/sign_up', method='POST')
@view('sign_up')
def create_user_sign_up():
    username = request.forms.get('username')
    password = request.forms.get('password')
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    birthdate = request.forms.get('birthdate')
    gender = request.forms.get('gender')

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'gender': gender
        }

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("INSERT INTO user (username, password, first_name, last_name, birthdate, gender) VALUES (?, ?, ?, ?, ?, ?)", (username, hashed, first_name, last_name, birthdate, gender))
    new_userid = c.lastrowid
    response.set_cookie('userid', new_userid, "teamfin")
    fhir = FHIR('http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base')
    fhir_id = fhir.create_new_patient(user)
    c.execute("UPDATE user SET fhir_id=? WHERE id=?", (fhir_id, int(new_userid)))
    db.commit()
    c.close()

    return fitBitConnect()
