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
