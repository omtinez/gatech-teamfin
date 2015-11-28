from bottle import route, view, request, response
from datetime import datetime
import sqlite3

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='JogRx is a student product at the Georgia Institute of Technology',
        year=datetime.now().year
    )
