from flask import request , Flask
import json
# from markupsafe import escape

app9 = Flask(__name__)
@app9.route('/')
def hello_world():
    return 'Hi this is app9'

if __name__=='__main__':
    app9.run(debug=True, host='0.0.0.0')