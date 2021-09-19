import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import uuid
from database import dataBase
import datetime

db = dataBase()

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask("ReBug")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    data, keys = db.get()
    return render_template('index.html')


@app.route('/report', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        location = request.form['location']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            fileName = str(uuid.uuid4())+".jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
            time = str(datetime.datetime.now() + datetime.timedelta(weeks=1))
            time = time[:time.index(" ")]
            db.add(location, 10, time)
            return render_template("thanks.html")
    data, keys = db.get()
    return render_template("report.html")

@app.route("/volunteer")
def volunteer():
    data, keys = db.get()
    return render_template("volunteer.html")
