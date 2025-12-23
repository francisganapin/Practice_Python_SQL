from flask import Flask,request,jsonify
import json
import os


app = Flask(__name__)

DATA_FILE = 'data.json'


if not os.path.exists(DATA_FILE):
    with open(DATA_FILE,'w') as f:
        json.dump([],f)


@app.route('/submit',methods=['POST'])
def submit_data():
    try:
        incoming_data = request.get_json()

        with open(DATA_FILE,'r') as f:
            data = json.load(f)
    
        data.append(incoming_data)

        with open(DATA_FILE,'w') as f:
            json.dump(data,f,indent=4)

        return jsonify({'message':"Data saved successfully!"}),201

    except Exception as e:
        return jsonify({'error':str(e)}),500
    

@app.route('/data/<id>',methods=['GET'])
def get_data_by_id(id):
    with open(DATA_FILE,'r') as f:
        data = json.load(f)

    for entry in data:
        if str(entry['id']) == id:
            return jsonify(entry)
        

    return jsonify({'error','Not found'}),404
    

@app.route('/data/<int:id>',methods=['PUT'])
def update_data_by_id(id):
    try:
        with open(DATA_FILE,'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return jsonify({'error':"Data file not found"}),500
    
    updated = False
    for entry in data:
        if entry['id'] == id:
            new_data = request.get_json()
            entry.update(new_data)
            updated = True
            break
    
    if not updated:
        return jsonify({'error':"Item not found"}),404

    with open(DATA_FILE,'w') as f:
        json.dump(data,f,indent = 4)

    return jsonify({'message':'Data updated successfuly','data':entry})

if __name__ == '__main__':
    app.run(debug=True)