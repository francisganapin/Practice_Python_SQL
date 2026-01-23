from flask import Flask,request,jsonify
import json
import os


app = Flask(__name__)
DATA_FILE = 'data2.json'


USERS = {
    'admin':'secret123',
    'francis':'password123'
}

def check_auth(username,password):
    return USERS.get(username) == password

def anauthorized():
    return jsonify({'error':'Unauthorized'}),401

def require_auth(func):
    def wrapper(*args,**kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username,auth.password):
            return anauthorized()
        return func(*args,**kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE,'w') as f:
        json.dump(data,f,indent=4)

@app.route('/data',methods=['GET'])
@require_auth
def get_data():
    return jsonify(load_data())


@app.route('/data',methods=['POST'])
@require_auth
def add_data():
    new_entry = request.get_json()
    data = load_data()
    data.append(new_entry)
    save_data(data)
    return jsonify({'message':"Added","data":new_entry}),201

if __name__ == '__main__':
    app.run(debug=True)