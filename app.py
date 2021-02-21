import flask
from flask import render_template
from process import process

app=flask.Flask(__name__, template_folder='templates/')
app.config["DEBUG"] = True


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/img_txt', methods=['POST', 'GET'])
def image_text_summary():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

app.run()
