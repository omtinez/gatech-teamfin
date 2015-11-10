"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

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

hisps = ["hitclass@hisp.i3l.gatech.edu","teamFinSpecialist@hisp.i3l.gatech.edu"]

def check_hisp(hisp):
    if hisp in hisps:
        return True
    else:
        return False

@route('/doctors_HISP', method='POST')
@view('doctors_HISP')
def do_doctors_HISP():
    hisp = request.forms.get('hispAddress')
    if check_hisp(hisp):
        return permissions()
    else:
        return doctors_HISP_failed()
	
@route('/permissions')
@view('permissions')
def permissions():
        return dict(
        title='Permissions',
        year=datetime.now().year
    )

@route('/permissions', method="POST")
@view('permissions')
def do_permissions():
    accept = request.forms.get('Accept')
    if  accept:
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
        message='Connect your Fitbit',
        year=datetime.now().year  
    )
	
fitBitUsernames = ["TeamFin"]
fitBitPasswords = ["TeamFin007"]

def check_fitBitLogin(username, password):
    if ((username in fitBitUsernames) and (password in fitBitPasswords)):
        return True
    else:
        return False
				 
@route('/fitBitConnect', method='POST')
@view('fitBitConnect')
def do_fitBitConnect():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_fitBitLogin(username, password):
        return success()
    else:
        return fitBitLogin_failed()

@route('/fitBitLogin_failed')
@view('fitBitLogin_failed')
def fitBitLogin_failed():
	return dict(
        title='FitBit Login Failed',
        year=datetime.now().year
    )
	
@route('/success')
@view('success')
def success():
	return dict(
        title='Success',
        year=datetime.now().year
    )

