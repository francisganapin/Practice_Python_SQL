from flask import Flask,jsonify


app = Flask(__name__)


@app.route('/hello',methods=['POST'])
def hello():
    return jsonify({"message":"Hello,JSON from Flask!"})


if __name__ == '__main__':
    app.run(debug=True)