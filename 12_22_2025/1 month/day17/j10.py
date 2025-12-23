from flask import Flask,request,jsonify
from functools import wraps

app = Flask(__name__)

user_db = {
    'admin':{'password':'admin123','token':'token-admin'},
    'user1':{'password':'user123','token':'token-user1'}
}

def require_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in [user['token'] for user in user_db.values()]:
            return jsonify({'error':'Unauthorized'}),401
        return f(*args,**kwargs)
    return decorated

@app.route('/profile',methods=['GET'])
@require_auth
def profile():
    return jsonify({"message":'welcome to your profile'})

if __name__  == '__main__':
    app.run(debug=True)