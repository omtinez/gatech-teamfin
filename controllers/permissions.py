from bottle import route, view, request, response
from datetime import datetime
import sqlite3
from success import success
from home import home

@route('/permissions')
@view('permissions')
def permissions():
    return dict(title='Permissions', year=datetime.now().year)

@route('/permissions', method="POST")
@view('permissions')
def do_permissions():
    accept = request.forms.get('Accept')
    userid = request.get_cookie("userid", secret='teamfin')
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    if accept:
        c.execute("UPDATE user SET accept_terms=? WHERE id=?", (1, int(userid)))
        db.commit()
        c.close()
        return success()
    else:
        c.execute("UPDATE user SET accept_terms=? WHERE id=?", (0, int(userid)))
        db.commit()
        c.close()
        return home()
