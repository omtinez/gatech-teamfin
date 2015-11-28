from bottle import route, view, request, response
from datetime import datetime
import sqlite3
from helpers import FHIR

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='JogRx is a student product at the Georgia Institute of Technology',
        year=datetime.now().year
    )


@route('/about', method='POST')
@view('about')
def do_about():
    fhir = FHIR('http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp/base')
    fhir.sync_with_fhir()
    return dict(
        title='Synced',
        message='JogRx was successfully synced with FHIR',
        year=datetime.now().year
    )
