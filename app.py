import flask
from flask import render_template
from process import process

app=flask.Flask(__name__, template_folder='templates/')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def image_captioning_function():
    return 'image captioning here'

@app.route('/', methods=['POST'])
def text_summarization():
    return 'text summaries here'

app.run()
