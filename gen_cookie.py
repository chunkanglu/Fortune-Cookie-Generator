from flask import Flask, render_template, make_response, request
from datetime import datetime, date, time, timedelta
app = Flask(__name__)

from random import randint

#opens cookie, returns fortune
@app.route('/')
def index():
    if (request.cookies.get("fortune") == None):
        fortune = openCookie()
        resp = make_response(render_template("index.html", fortune=fortune))
        resp.set_cookie("fortune", fortune, expires=get_midnight())
        return resp
    else:
        return render_template("index.html", fortune=request.cookies.get("fortune"))

# @app.route('/fortune')

def get_midnight():
    today_date = date.today()
    return datetime.combine(today_date + timedelta(days=1), time()) + timedelta(hours=4) # time() defaults to midnight UTC, +4 for EST

def openCookie() -> str:
    with open("fortunes.txt", "r") as fortunes:
        arr = fortunes.readlines()
        return arr[randint(0, len(arr) - 1)]

if __name__ == '__main__':
  app.run(debug=True)