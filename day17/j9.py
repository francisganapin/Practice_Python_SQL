from flask import Flask,request,jsonify

app = Flask(__name__)

data_store = []

@app.route('/items',methods=['POST'])
def add_item():
    new_item = request.get_json()
    data_store.append(new_item)
    return jsonify({'message':'item added','data':new_item}),201

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(data_store),200

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    if 0 <= item_id < len(data_store):
        return jsonify(data_store[item_id])
    return jsonify({'error':'Item not found'}),404

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(data_store):
        update = request.get_json()
        data_store[item_id].update(update)
        return jsonify({"message":"Item updated","data":data_store[item_id]})
    return jsonify({'error':'Item not found'}),404

@app.route('/item/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(data_store):
        deleted = data_store.pop(item_id)
        return jsonify({'message':'Item deleted','data':deleted})
    

if __name__ == '__main__':
    app.run(debug=True)