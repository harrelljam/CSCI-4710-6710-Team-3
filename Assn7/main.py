import os
import numpy
from flask import Flask, render_template, session, request
import util

app = Flask(__name__)
app.secret_key = 'dev'


@app.route("/")
def index():
    if 'userid' not in session:
        userId="id"
        return render_template("index.html", wrongCredentials=False, userInSession=True, getUserName=session['userid'])
    else:
        return render_template("index.html")

def userInSession():
    if 'userid' not in session:
        return false
    else:
        return true

# verify a string function is actually computable
def verify():
    funcstring = request.form['func-text']
    funcrun = request.form['func-run']
    # determine validity of the function
    print("Got a function {}".format(funcstring))
    return True


@app.route("/run", methods=['POST'])
# parse and compute the function, storing results in the session
# as well as the users history table
def run():
    # demo function f(x) = x, store 100 datapoints
    demo = {'func': 'X', 'data': [i for i in numpy.linspace(-10, 10, 100, endpoint=True)]}
    session['results'] = demo
    print(session['results']['data'])
    return render_template("index.html", function=session['results'])


@app.route("/history", methods=['GET'])
# retrieve a previously ran function from the users history
def getHistory():
    # demo just returns the same function, actual implementation
    # could return an object containing the name of the ran
    # function, along with 100 datapoints from running that
    # function, this should not actually need to compute anything
    return render_template("index.html", function=session['results'])


@app.route("/login", methods=['POST'])
def loginF():
    print("logis started")
    if not (util.correctCredentials(request.form['login'], request.form['password'])):
        session.clear()
        return render_template("index.html", wrongCredentials=True)
    else:
        return render_template("index.html", wrongCredentials=False, userInSession=True, getUserName=session['userid'])



@app.route("/register", methods=['POST'])
def registerF():
    print("register started")
    print("login"+request.form['loginR'])
    if not (util.correctCredentials(request.form['loginR'], request.form['passwordR'])):
        util.insertUser(request.form['loginR'], request.form['passwordR'],request.form['first_name'], request.form['last_name'])
        return render_template("index.html", UserExist=False)
    else:
        return render_template("index.html", UserExist=False)


# run application
if __name__ == "__main__":
    app.run(debug=True)
