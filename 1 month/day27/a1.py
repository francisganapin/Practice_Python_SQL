import sqlite3
from flask import Flask,request,jsonify


app = Flask(__name__)
DATABASE = 'user.db'



def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
                CREATE TABLE IF NOT EXISTS USER(
                 id INTEGER Primary Key,
                 name TEXT NOT NULL,
                 age integer NOT NULL
                 )
""")
    conn.commit()
    conn.close()


init_db()

@app.route('/add_user',methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error":"No input data provide"}),400
    
    required_field = ['id','name','age']
    for field in required_field:
        if field not in data:
            return jsonify({"error":f"Missing Field:{field}"}),400
        
    if not isinstance(data['age'],int) or data['age'] <= 0:
        return jsonify({'error':"Age must be a possitive integer"}),400
    
    try:
        conn = get_db_connection()
        conn.execute("Insert into user(id,name,age) VALUES(?,?,?)",
                     (data['id'],data['name'],data['age']))
        conn.commit()
        conn.close()
        return jsonify({"message":"User added successfully",'user':data}),201

    except sqlite3.IntegrityError as e:
        return jsonify({'error':f'Data integrity error: {str(e)}'}),400

    except Exception as e:
            return jsonify({'error':f"Something went wrong: {str(e)}"}),500
    

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM USER').fetchall()
    conn.close()
    return jsonify([dict(row) for row in users]), 200

if __name__ == '__main__':
    app.run(debug=True)