from flask import Flask,jsonify,request
import json
import os


app = Flask(__name__)
DATA_FILE = 'data2.json'


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


# insert data 
@app.route('/data',methods=['POST'])
def add_data():
    new_entry = request.get_json()
    data = load_data()
    data.append(new_entry)
    save_data(data)
    return jsonify({'message':"added","data":new_entry}),201

#load all data
@app.route('/data',methods=['GET'])
def get_all_data():
    return jsonify(load_data())

@app.route('/data/<int:item_id>',methods=['GET'])
def get_one(item_id):
    data = load_data()
    for item in data:
        if item.get('id') == item_id:
            return jsonify(item)
    return jsonify({'error':'item not found'}),404


#get data using id
@app.route('/data/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    data =load_data()
    update = request.get_json()
    for index,item in enumerate(data):
        if item.get('id') == item_id:
            data[index].update(update)
            save_data(data)
            return jsonify({'message':'Updated','data':data[index]})
    return jsonify({'error':'item not found'}),404



@app.route('/data/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    data = load_data()
    for item in data:
        if item.get('id') == item_id:
            data.remove(item)
            save_data(data)
            return jsonify({'message':'Deleted','id':item_id})
    return jsonify({'error':"item not found"}),404



if __name__ == '__main__':
    app.run(debug=True)