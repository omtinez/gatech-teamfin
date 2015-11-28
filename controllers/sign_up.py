from bottle import route, view, request, response
from datetime import datetime
import sqlite3
import bcrypt
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

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    # new_userid = c.lastrowid
    c.execute("INSERT INTO user (username, password, first_name, last_name) VALUES (?, ?, ?, ?)", (username, hashed, first_name, last_name));
    new_userid = c.lastrowid
    db.commit()
    c.close()
    # TODO: where should the user go after this?
    response.set_cookie('userid', new_userid, "teamfin")
    return fitBitConnect()
