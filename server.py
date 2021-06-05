from typing import Set
from flask import Flask, render_template
from flask import request
from datetime import datetime, timedelta

import db

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    print(request.args.get("lightStatus"))
    print(request.args.get("test"))
    lightStatus = str(request.args.get("lightStatus"))
    lightValue = str(request.args.get("lightValue"))
    soundValue = str(request.args.get("soundValue"))
    mystr = f"Light Status: {lightStatus}\nLight Value: {lightValue}\nSound Value: {soundValue}"
    print(mystr)

    db.addData(lightValue, lightStatus, soundValue)

    return render_template('index.html')

@app.route("/data", methods=['GET', 'POST'])
def index():
    dates = []
    lightValue = []
    soundValue = []
    lightStatus = []

    data = db.getLightValue()
    for i in data:
        date = i[2] - timedelta(hours=7)
        date = date.strftime("%I:%M:%S%p")
        dates.append(date)

        lightValue.append(str(i[1]))
    
    data = db.getSoundValue()
    for i in data:
        soundValue.append(str(i[1]))

    data = db.getLightStatus()
    for i in data:
        lightStatus.append(str(i[1]))

    dates = " ".join(dates)
    lightValue = " ".join(lightValue)
    soundValue = " ".join(soundValue)
    lightStatus = " ".join(lightStatus)


    return render_template('index.html', xlabels=dates, lightValue=lightValue, soundValue=soundValue, lightStatus=lightStatus)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")