from bottle import route, view, request, response
from datetime import datetime
import sqlite3
from permissions import permissions

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
    server = request.forms.get('hispAddress').strip()
    userid = request.get_cookie("userid", secret='teamfin')
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("UPDATE user SET server=? WHERE id=?", (server, int(userid)))
    db.commit()
    c.close()
    return permissions()
