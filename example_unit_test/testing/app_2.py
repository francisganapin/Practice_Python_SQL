from flask import Flask,jsonify,request


app = Flask(__name__)


foods = [
    {'id':1,'name':'Apple','calories':95},
    {'id':2,"name":'Banana','Calories':105}
]

@app.route('/')
def home():
    return jsonify({"message":"Welcome to the Food Api"})

@app.route("/foods",methods=['GET'])
def get_food():
    return jsonify(foods)


@app.route("/foods/<int:food_id>",methods=['GET'])
def get_food_by_id(food_id):
    food = next((f for f in foods if f['id'] == food_id),None)
    return jsonify(food) if food else jsonify({"error":"Food not Found"}),404


@app.route('/foods',methods=['POST'])
def add_food():
    data = request.get_json()
    new_food  ={
        'id':len(foods) + 1,
        'name':data['name'],
        'calories':data['calories']
    }
    foods.append(new_food)
    return jsonify(new_food),201


@app.route('/foods/<int:food_id>',methods=['PUT'])
def update_food(food_id):
    food = next((f for f in foods if f['id'] == food_id),None)
    if not food:
        return jsonify({"error":"Food not found"}),404

    data = request.get_json()
    food['name'] = data.get('name',food['name'])
    food['calories'] = data.get('calories',food['calories'])
    return jsonify(food)

@app.route('/foods/<int:food_id>',methods=['DELETE'])
def delete_food(food_id):
    global foods
    foods = [f for f in foods if f['id'] != food_id]
    return jsonify({"message":"Food deleted"})


if __name__ == '__main__':
    app.run(debug=True)