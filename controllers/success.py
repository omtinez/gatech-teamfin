from bottle import route, view, request, response
from datetime import datetime
import sqlite3

@route('/success')
@view('success')
def success():
    return dict(title='Success', year=datetime.now().year)
