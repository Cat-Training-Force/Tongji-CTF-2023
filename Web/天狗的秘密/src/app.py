from flask import Flask, render_template, request, session, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'dalpdqdqd-#%^cazcsad;asdafad'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/change_username', methods=['POST'])
def change_username():
    username = request.form['username']
    session['username'] = username
    session['pri'] = "normal"
    return redirect(url_for('index'))


@app.route('/read_secret',methods=['GET'])
def read_key():
    path = request.args.get("path")
    if path == None:
        path = "static/secrets"
    else: 
        pattern = re.compile(r'\.\./|\.\.|\\')
        
        if pattern.search(path):
            return "No hacker!"
        
        pattern = re.compile(r'flag')
        if pattern.search(path) and session['pri'] != 'nvshen':
            return "No hacker!"
                
    with open(path,"r", encoding='utf-8') as fin:
        secrets = fin.read()
    return "不准告诉别人哦，{}".format(secrets)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000",debug=True)