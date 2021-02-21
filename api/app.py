import flask 
app=flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>BLueprint Project</h1><p>hello world .</p>"

@app.route('/', methods=['POST'])
def image_captioning_function():
    return 'image captioning here'

@app.route('/', methods=['POST'])
def text_summarization():
    return 'text summaries here'

app.run()