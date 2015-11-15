"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, response
from datetime import datetime
import sqlite3


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )


@route('/sign_up', method='GET')
@view('sign_up')
def get_sign_up():
    return dict(year=datetime.now().year)


@route('/sign_up', method='POST')
@view('sign_up')
def create_user_sign_up():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print username
    print password
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    # new_userid = c.lastrowid
    c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
    new_userid = c.lastrowid
    db.commit()
    c.close()
    # TODO: where should the user go after this?
    response.set_cookie('userid', new_userid, "teamfin")
    return fitBitConnect()


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


@route('/loginFailed')
@view('loginFailed')
def login_failed():
    return dict(
        title='Login failed',
        year=datetime.now().year
    )


@route('/doctors_HISP')
@view('doctors_HISP')
def doctors_HISP():
    return dict(
        title='Connect with your doctor',
        message='',
        year=datetime.now().year
    )


@route('/doctors_HISP', method='POST')
@view('doctors_HISP')
def do_doctors_HISP():
    hisp = request.forms.get('hispAddress').strip()
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("INSERT INTO hisp (server) VALUES (?)", (hisp,))
    new_id = c.lastrowid
    db.commit()
    c.close()
    # TODO: where should the user go after this?
    return about()


@route('/permissions')
@view('permissions')
def permissions():
        return dict(title='Permissions', year=datetime.now().year)


@route('/permissions', method="POST")
@view('permissions')
def do_permissions():
    accept = request.forms.get('Accept')
    if accept:
        return fitBitConnect()
    else:
        return home()


@route('/doctor_HISPFailed')
@view('doctor_HISPFailed')
def doctors_HISP_failed():
    return dict(
        title='Connection with you doctor failed',
        message='Invalid doctors HISP address',
        year=datetime.now().year
    )


@route('/fitBitConnect')
@view('fitBitConnect')
def fitBitConnect():
    return dict(
        message='Connect your Fitbit', year=datetime.now().year)


@route('/fitBitConnect', method='POST')
@view('fitBitConnect')
def do_fitBitConnect():
    fitbit_username = request.forms.get('username')
    # TODO we should check if its a valid Fitbit name
    userid = request.get_cookie("userid", secret='teamfin')
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    print userid
    print fitbit_username
    c.execute("UPDATE user SET fitbit_username=? WHERE id=?", (fitbit_username, int(userid)))
    db.commit()
    c.close()
    return fitBitConnect()


@route('/success')
@view('success')
def success():
    return dict(title='Success', year=datetime.now().year)
