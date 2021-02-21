import os
from os.path import join, dirname, realpath
import flask
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from process import process

UPLOAD_FOLDER = 'uploads/'
UPLOADS_PATH = join(dirname(realpath(__file__)), 'uploads/..')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app=flask.Flask(__name__, template_folder='templates/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/process', methods=['POST'])
def image_text_summary():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return
app.run()
