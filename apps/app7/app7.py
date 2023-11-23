from flask import request , Flask
import json
# from markupsafe import escape

app7 = Flask(__name__)
@app7.route('/')
def hello_world():
    return 'Hi this is app7'

if __name__=='__main__':
    app7.run(debug=True, host='0.0.0.0')