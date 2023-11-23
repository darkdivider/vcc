from flask import request , Flask
import json
# from markupsafe import escape

app8 = Flask(__name__)
@app8.route('/')
def hello_world():
    return 'Hi this is app8'

if __name__=='__main__':
    app8.run(debug=True, host='0.0.0.0')