from flask import request , Flask
import json
# from markupsafe import escape

app4 = Flask(__name__)
@app4.route('/')
def hello_world():
    return 'Hi this is app4'

if __name__=='__main__':
    app4.run(debug=True, host='0.0.0.0')