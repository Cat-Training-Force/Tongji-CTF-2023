#!flask/bin/python
from flask import Flask, Response, jsonify, render_template, request
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from hashlib import sha256
from time import sleep
import os

PORT = 17001

SECRET_LOCATION = 'secret.txt'

original_flag = open(SECRET_LOCATION).read().strip()
print(original_flag)

# import os
# new_flag = os.environ.get('GZCTF_FLAG', original_flag)
# print(new_flag)
# open(SECRET_LOCATION, 'w').write(new_flag)



app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()


def calc_sha256(b):
    s = sha256()
    s.update(b.encode('utf-8'))
    return s.hexdigest()


@app.route('/answer', methods=['POST'])
@cross_origin()
def answer():
    sleep(1)
    try:
        data = request.form.to_dict(flat=False)
        ans_hash = calc_sha256(str(data))
        print(str(data))
        print(ans_hash)
        assert ans_hash == '87bb1eeadf8f5c40b2b83b8c3f7ff2e92f97eff47c74a563a13a8c774b40a1dc'
        ret = {
            "status": 0,
            "msg": original_flag,
        }
        return jsonify(ret)
    except:
        ret = {
            "status": 1,
            "msg": '答案不对喵～',
            # "msg": calc_sha256(str(data)),
        }
        return jsonify(ret)


@app.route("/")
def main():
    return render_template("main.html", port=PORT)


# CORS(app, resources=r'/*')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=str(PORT))
