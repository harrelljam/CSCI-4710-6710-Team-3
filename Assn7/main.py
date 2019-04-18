import os
import re
import numpy
from flask import Flask, render_template, session, request
import util

app = Flask(__name__)
app.secret_key = 'dev'


@app.route("/")
def index():
    if 'userid' in session:
        return render_template("index.html", wrongCredentials=False, userInSession=True, getUserName=session['userid'])
    else:
        return render_template("index.html")


def userInSession():
    return 'userid' in session


@app.route("/run", methods=['POST'])
# parse and compute the function, storing results in the session
# as well as the users history table
def run():
    # demo function f(x) = x, store 100 datapoints
    X_values = [i for i in numpy.linspace(-10, 10, 100, endpoint=True)]
    Y_values = []
    for X in range(100):
        func = request.form['func-text']
        replaced = func.replace("X", "("+str(X_values[X])+")").replace("^","**")
        Y_values.append(eval(replaced))
    session['results'] = {
        'func': request.form['func-text'],
    }
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
    print("login started")
    if not (util.correctCredentials(request.form['login'], request.form['password'])):
        session.clear()
        return render_template("index.html", wrongCredentials=True)
    else:
        return render_template("index.html", wrongCredentials=False, userInSession=True, getUserName=session['userid'])


@app.route("/register", methods=['POST'])
def registerF():
    print("register started")
    print("login" + request.form['loginR'])
    if not (util.correctCredentials(request.form['loginR'], request.form['passwordR'])):
        util.insertUser(request.form['loginR'], request.form['passwordR'], request.form['first_name'],
                        request.form['last_name'])
        return render_template("index.html", UserExist=False)
    else:
        return render_template("index.html", UserExist=False)


# run application
if __name__ == "__main__":
    app.run(debug=True)
