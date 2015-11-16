from bottle import route, view, request, response
from datetime import datetime
import sqlite3

@route('/loginFailed')
@view('loginFailed')
def login_failed():
    return dict(
        title='Login failed',
        year=datetime.now().year
    )
