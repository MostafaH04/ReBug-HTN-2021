import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

uploadFolder = './images'
allowedFiles = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask("ReBug")
app.config['uploadFolder'] = uploadFolder

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowedFiles

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['uploadFolder'], filename))
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>ReBug</title>
    <h1>Upload site image</h1>
    <form method=post enctype=multipart/form-data>
    <input type="file">
    <input type=submit value="Submit Image">
    </form>
    '''

@app.route('/events')
def title():
    return '''
    <body style = "display: flex; background-color: white; justify-content: center;">
    <h2 style = "font-family: montserrat; color: orange; font-weight: 800;">Volunteering Oppurtunites</h2>
    </body>
    '''