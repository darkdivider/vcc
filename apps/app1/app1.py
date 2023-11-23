from flask import request , Flask
import json
import time
# from markupsafe import escape

app1 = Flask(__name__)
@app1.route('/')
def hello_world():
    time.sleep(0.05)
    return 'Hi this is app1'

if __name__=='__main__':
    app1.run(debug=True, host='0.0.0.0')