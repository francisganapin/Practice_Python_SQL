from flask import Flask,request,jsonify
import json

app = Flask(__name__)

with open('users.json','r') as file:
    users = json.load(file)

@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users),200

@app.route('/users',methods=['POST'])
def add_user():
    data = request.get_json()

    #check if email is exist
    new_email = data.get('email')
    existing_email = next((email for email in users if email['email'] == new_email),None)
    if existing_email:
        return jsonify({'error':'Email already exist'})

    #Generate new User ID
    new_id = max([u['id'] for u in users],default=0) + 1

    new_user = {
        'id': new_id,
        'name': data.get('name'),
        'email': new_email
    }

    users.append(new_user)  # Correctly add the new user to list

    with open('users.json','w') as file:
        json.dump(users,file,indent=4)

    return jsonify({'message':'User added!','user':data}),201

@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error':'User not found'}),404
    
    user['name'] = data.get('name',user['name'])
    user['email'] = data.get('email',user['email'])

    with open('users.json','w') as file:
        json.dump(users,file,indent=4)

    return jsonify({'message':'User Update!','user':user}),200

@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    users = ''
    
    user = next((u for u in users if u['id'] == user_id),None)
    if not user:
        return jsonify({'error':'User not Found'}),404

    users = [u for u in users if u["id"] != user_id]  # Remove user

    with open('users.json','w') as file:
        json.dump(users,file,indent=4)

    return jsonify({"message":'User delete!'}),200

if __name__ == '__main__':
    app.run(debug=True)