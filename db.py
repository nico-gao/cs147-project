from flask import Flask
from flaskext.mysql import MySQL
from datetime import datetime
import pymysql

import configuration as config

# app = Flask(__name__)

# app.config['MYSQL_DATABASE_HOST'] = configuration.mysql_host
# app.config["MYSQL_DATABASE_USER"] = configuration.mysql_user
# app.config['MYSQL_DATABASE_PASSWORD'] = configuration.mysql_password
# app.config['MYSQL_DATABASE_DB'] = configuration.mysql_db

# mysql = MySQL()
# mysql.init_app(app)

db = pymysql.connect(host=config.mysql_host, 
                    user = config.mysql_user, 
                    password = config.mysql_password,
                    database = config.mysql_db)


def addData(lightValue, lightStatus, soundValue):
    query1 = f"INSERT INTO LightValue (lightValue) VALUES ({lightValue})"
    query2 = f"INSERT INTO LightStatus (lightStatus) VALUES ({lightStatus})"
    query3 = f"INSERT INTO SoundValue (soundValue) VALUES ({soundValue})"
    print(query1)
    cur = db.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    db.commit()
    print("NEW DATA ADDED!")

def getLightStatus():
    cur = db.cursor()
    cur.execute("SELECT * FROM LightStatus")
    data = cur.fetchall()
    return data

def getLightValue():
    cur = db.cursor()
    cur.execute("SELECT * FROM LightValue")
    data = cur.fetchall()
    return data

def getSoundValue():
    cur = db.cursor()
    cur.execute("SELECT * FROM SoundValue")
    data = cur.fetchall()
    return data   