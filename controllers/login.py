from bottle import route, view, request, response
from datetime import datetime
import sqlite3
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
    c.execute("Select * from user where username = ? and password = ?", (username, password,))
    result = c.fetchone()
    return result


@route('/login', method='POST')
@view('login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password)is None:
        return login_failed()
    else:
        return success()
