from flask import Flask,request,jsonify


app = Flask(__name__)


@app.route('/api/greet',methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name','Guest')
    return jsonify({"message":f"Hello,{name}!"})


if __name__ == '__main__':
    app.run(debug=True)