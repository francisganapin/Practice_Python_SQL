from flask import Flask,jsonify,request
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

@app.route('/data',methods=['POST'])
def add_data():
    new_entry = request.get_json()

    data = load_data()
    data.append(new_entry)

    with open(DATA_FILE,'w') as f:
        json.dump(data,f,indent=4)

    return jsonify({'message':"Added","data":new_entry}),201


if __name__ == '__main__':
    app.run(debug=True)