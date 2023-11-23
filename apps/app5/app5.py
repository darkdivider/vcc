from flask import request , Flask
import json
# from markupsafe import escape

app5 = Flask(__name__)
@app5.route('/')
def hello_world():
    return 'Hi this is app5'

if __name__=='__main__':
    app5.run(debug=True, host='0.0.0.0')