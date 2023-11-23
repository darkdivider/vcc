from flask import request , Flask
import json
# from markupsafe import escape

app3 = Flask(__name__)
@app3.route('/')
def hello_world():
    return 'Hi this is app3'

if __name__=='__main__':
    app3.run(debug=True, host='0.0.0.0')