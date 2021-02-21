import flask 
app=flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home', methods=['GET'])
def home():
    return "<h1>BLueprint Project</h1><p>hello world .</p>"

@app.route('/img_txt', methods=['POST', 'GET'])
def image_text_summary():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
 

    return 'RESULTS here'
   
app.run()