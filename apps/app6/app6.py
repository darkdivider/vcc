from flask import request , Flask
import json
# from markupsafe import escape

app6 = Flask(__name__)
@app6.route('/')
def hello_world():
    return 'Hi this is app6'

if __name__=='__main__':
    app6.run(debug=True, host='0.0.0.0')