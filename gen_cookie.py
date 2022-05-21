from flask import Flask, render_template, make_response, request
app = Flask(__name__)

from random import randint

#opens cookie, returns fortune
@app.route('/')
def index():
    if (request.cookies.get("fortune") == None):
        fortune = openCookie()
        resp = make_response(render_template("index.html", fortune=fortune))
        resp.set_cookie("fortune", fortune)
        return resp
    else:
        return render_template("index.html", fortune=request.cookies.get("fortune"))

@app.route('/fortune')
def openCookie() -> str:
    with open("fortunes.txt", "r") as fortunes:
        arr = fortunes.readlines()
        return arr[randint(0, len(arr) - 1)]

if __name__ == '__main__':
  app.run(debug=True)

print(openCookie())