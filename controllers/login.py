from bottle import route, view, request, response
from datetime import datetime
import sqlite3
import bcrypt
from loginFailed import login_failed
from success import success

@route('/login')
@view('login')
def login():
    return dict(
        message='Enter your email to get started',
        year=datetime.now().year
    )
usernames = ["TeamFin@gtech.edu"]
passwords = ["TeamFin007"]

def check_login(username, password):
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("Select id, password from user where username = ?", (username,))
    row = c.fetchone()
    if row is not None:
        hashed = row[1].encode('utf-8')
        if bcrypt.hashpw(password, hashed) == hashed:
            return row[0]

    return None
        


@route('/login', method='POST')
@view('login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    user_id = check_login(username, password)
    if user_id:
        response.set_cookie('userid', user_id, "teamfin")
        return success()
    else:
        return login_failed()
