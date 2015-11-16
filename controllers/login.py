from bottle import route, view, request, response
from datetime import datetime
import sqlite3

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
    if ((username in usernames) and (password in passwords)):
        return True
    else:
        return False

@route('/login', method='POST')
@view('login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return doctors_HISP()
    else:
        return login_failed()
