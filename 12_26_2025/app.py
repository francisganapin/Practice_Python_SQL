from flask import Flask,jsonify,render_template
import time
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    
    time.sleep(2)
    return jsonify({'message':'Hello from Flask!','status':'success'})

@app.route('/api/data2')
def get_data2():

    time.sleep(2)
    return jsonify({'message':'Hello from Flask2','status':'pending'})



if __name__ == '__main__':
    app.run(debug=True)