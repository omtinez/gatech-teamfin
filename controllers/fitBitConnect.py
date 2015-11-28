from bottle import route, view, request, response
from datetime import datetime
import sqlite3
from doctors_HISP import doctors_HISP
from loginFailed import login_failed
@route('/fitBitConnect')
@view('fitBitConnect')
def fitBitConnect():
    return dict(message='Connect your Fitbit', year=datetime.now().year)


@route('/fitBitConnect', method='POST')
@view('fitBitConnect')
def do_fitBitConnect():
    fitbit_id = request.forms.get('username')
    # TODO we should check if its a valid Fitbit name
    userid = request.get_cookie("userid", secret='teamfin')
    # TODO refactor the db out and pass in as an argument to sign_up method
    db = sqlite3.connect('database/jogrx.db')
    c = db.cursor()
    c.execute("Select id from steps where username = ?", (fitbit_id,))
    row = c.fetchone()
    if row is None:
        c.execute("UPDATE user SET fitbit_id=? WHERE id=?", (fitbit_id, int(userid)))
        c.execute("INSERT INTO steps (username) VALUES ('%s')"%(fitbit_id))
        db.commit()
        c.close()
        return doctors_HISP()
    else:
        c.close()
        return login_failed()

