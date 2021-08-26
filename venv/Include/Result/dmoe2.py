from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/test',methods=['POST'])
def test():
    jsonstr = json.loads(request.get_data())
    print(jsonstr)
    return json.dumps({
        'code':200,
        'msg':'success'
    })

if __name__ == '__main__':
    app.run()