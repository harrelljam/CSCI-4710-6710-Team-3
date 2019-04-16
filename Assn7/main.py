import os
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/verify",methods=['POST'])
#verify a string function is actually computable
def verify():
	return render_template("index.html",verified=True)

@app.route("/run",methods=['POST'])
#parse and compute the function, storing results in the session
#as well as the users history table
def run():
	#demo function f(x) = x, store 100 datapoints
	session['results'] = {
		func:'x',
		data:[i for i in range(-10,10,0.1)]
	}
	return render_template("index.html",function=session['results'])

@app.route("/history",methods=['GET'])
#retrieve a previously ran function from the users history
def getHistory():
	#demo just returns the same function, actual implementation
	#could return an object containing the name of the ran
	#function, along with 100 datapoints from running that
	#function, this should not actually need to compute anything
	return render_template("index.html",function=session['results'])

@app.route("/login",methods=['GET','POST'])
#login
def login():
	return render_template("login.html")

@app.route("/register",methods=['GET','POST'])
def register():
	return render_template("register.html")


#run application
if __name__ == "__main__":
	app.run(debug=True)
