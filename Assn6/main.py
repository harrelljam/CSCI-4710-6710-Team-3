import os
from flask import Flask, request, render_template, redirect, url_for, g, session
from werkzeug.utils import secure_filename
import util

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/data/'

app = Flask(__name__)
app.secret_key = 'myapp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/verify", methods=['GET', 'POST'])
def verify():
    # print(session.get('filename', None))
    if 'filename' not in session:
        log = 'no file field in request.'
        return render_template('fail.html', log=log)
    else:
        filename = secure_filename(session.get('filename', None))
        column_names, data_part = util.preview_csv(app.config['UPLOAD_FOLDER'] + filename)
        return render_template('verify.html', column_names=column_names, data_part=data_part)


@app.route("/configure", methods=['GET', 'POST'])
def configure():
    print(request.form)
    if 'filename' not in session:
        log = 'no file field in request.'
        return render_template('fail.html', log=log)
    else:
        filename = secure_filename(session.get('filename', None))
        column_names, data_part = util.preview_csv(app.config['UPLOAD_FOLDER'] + filename)
        return render_template('configure.html', selected_columns=column_names)


@app.route("/runtests", methods=['GET', 'POST'])
def runtests():
    return render_template('runtests.html')

@app.route("/review", methods=['GET','POST'])
def review():
    return render_template('review.html')

@app.route('/api/post_csv', methods=['POST'])
def post_csv():
    if 'proceed' in request.form:
        print('yes!')
    # request.file <class 'werkzeug.datastructures.FileStorage'>
    # request.url is http://127.0.0.1:5000/api/post_csv
    # check if the post request has the file part
    # print("entered post")
    if 'file' not in request.files:
        log = 'no file field in request.'
        return render_template('fail.html', log=log)
    # print(request.files['file'])
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        log = 'Empty filename.'
        return render_template('fail.html', log=log)
    # print ("filename is not empty")
    if file and util.allowed_file(file.filename):
        # get filename in a safe way
        print("filename")
        filename = secure_filename(file.filename)
        # print(filename)
        # check if the data folder exists, if not create one
        # print(UPLOAD_FOLDER)
        if os.path.exists(app.config['UPLOAD_FOLDER']) == False:
            # print("folder does not exist")
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        g.filename = filename
        session['filename'] = filename
        return render_template('index.html', filename=filename)
    print("Not CSV")
    log = 'Not CSV.'
    # return False
    return render_template('index.html', log=log)

@app.route("/api/runtests",methods=['POST'])
def test():
    demotest = [
        {
            'x':1,
            'y':10,
            'pass':True
        },
        {
            'x':2,
            'y':10,
            'pass':True
        },
        {
            'x':3,
            'y':5,
            'pass':True
        },
        {
            'x':4,
            'y':2,
            'pass':False
        },
        {
            'x':5,
            'y':1,
            'pass':False
        },
    ]
    session['testres'] = demotest
    return render_template('runtests.html')

if __name__ == "__main__":
    app.run(debug=True)
