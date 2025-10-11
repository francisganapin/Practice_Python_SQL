from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/add_user',methods=['POST'])
def add_user():

    data = request.get_json()

    if not data:
        return jsonify({"error":"No input data provided"}),400
    
    required_fields = ['id','name','age']
    for field in required_fields:
        if field not in data:
            return jsonify({"error":f"Missing Field:{field}"}),400
        

    if not isinstance(data['age'],int) or data['age'] <= 0:
        return jsonify({'error':"Age must be possitive integer"}),400

    return jsonify({
        "message":"User added successfully",
        "user":data
    }),201


if __name__ == "__main__":
    app.run(debug=True)