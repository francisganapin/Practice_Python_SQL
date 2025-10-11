from flask import Flask,request,jsonify

import json
import os


app = Flask(__name__)
DATA_FILE = 'data.json'


USERS = {
    'admin':'secret123',
    'well':'password123'
}

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if USERS.get(username) == password:
        return jsonify({
            "message":"Login successful",
            "user":username

        }),200
    else:
        return jsonify({"error":'invalid user or password'}),401
