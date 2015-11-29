import sqlite3;
import datetime;
import random;

class DBAPI:
    def __init__(self):
        self.dbName = "jogrx.db"

    def insertSteps(self, username, curTime, numSteps):
        db = sqlite3.connect('database/%s'%self.dbName)
        c = db.cursor()
        exeStatement = "INSERT INTO steps (username, retrieveTime, stepsTaken) VALUES ('%s','%s','%s')"%(username, curTime, numSteps)
        c.execute(exeStatement)
        db.commit()
        c.close()

    def getSteps(self, username):
        db = sqlite3.connect('database/%s'%self.dbName)
        c = db.cursor()
        exeStatement = "SELECT retrieveTime, stepsTaken, username FROM steps WHERE username=='%s'" %(username)
        c.execute('Select retrieveTime, stepsTaken, username from steps where username = ?', [username])
        stepData = c.fetchall()
        c.close()
        ret = {};

        # we should only get data for this user
        for stepRow in stepData:
            curTime, steps, rowUserName = stepRow

            if rowUserName == username:
                ret[curTime] = steps;
        return str(stepData);


    def insertBMI(self, username, weightIBS, heightInches):
        db = sqlite3.connect('database/%s'%self.dbName)
        c = db.cursor()

        weightChange = weightIBS * 0.45
        heightChange = heightInches * 0.025
        bmi = weightChange / (heightChange * heightChange)

        updateStatement = "INSERT INTO bmi (username, weight, height, bmi) VALUES ('%s','%s','%s','%s')"%(username, weightIBS, heightInches, bmi)
        c.execute(updateStatement)
        db.commit()
        c.close()

    def updateBMI(self, username, weightIBS, heightInches):
        db = sqlite3.connect('database/%s'%self.dbName)
        c = db.cursor()

        weightChange = weightIBS * 0.45
        heightChange = heightInches * 0.025
        bmi = weightChange / (heightChange * heightChange)

        updateStatement = "UPDATE bmi set username='%s', weight='%s', height='%s', bmi='%s' where username='%s'"%(username, weightIBS, heightInches, bmi, username)
        c.execute(updateStatement)
        db.commit()
        c.close()

    def getBMI(self, username):
        db = sqlite3.connect('database/%s'%self.dbName)
        c = db.cursor()
        c.execute("Select weight, height, bmi, username from bmi where username=='%s'"%username)
        row = c.fetchone()
        c.close()

        ret = {};
        weight, height, bmi, curUsername = row

        if curUsername == username:
            ret["Weight"] = weight;
            ret["Height"] = height;
            ret["BMI"] = bmi;
        return ret;

if __name__ == "__main__":
    username = "fakeUser"
    db = DBAPI();

    for i in range(10):
        # some steps for the day
        steps = random.randint(100, 1000);
        # current date time
        dtNow = unicode(datetime.datetime.now())
        db.insertSteps(username, dtNow, steps);

    print db.getSteps(username);
    assert len(db.getSteps("fake2")) == 0

    # db.insertBMI(username, 180, 90);

    db.updateBMI(username, 125, 63);
    assert db.getBMI(username)["BMI"] == 22.6757369615

    db.updateBMI(username, 180, 74);
    assert db.getBMI(username) == 23.6669101534