from flask import request , Flask
import json
# from markupsafe import escape

app10 = Flask(__name__)
@app10.route('/')
def hello_world():
    return 'Hi this is app10'

if __name__=='__main__':
    app10.run(debug=True, host='0.0.0.0')