from flask import Flask,request,jsonify
from sqlmodel import Session,SQLModel,create_engine,select
from models import GymMember 

from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
DATABASE_URL = 'sqlite:///gym_members.db'
engine = create_engine(DATABASE_URL,echo=True)


# create Member
@app.route('/members/create',methods=['POST'])
def create_member():
    data = request.get_json()
    member = GymMember(**data)
    #check if post is complete 

    if len(data.get('key_code', '')) != 6:
        return jsonify({"error":f" key code must 6 character  "}),400
    
    required_fields = ['key_code','first_name','last_name','phone','membership_type']
    for field in required_fields:
        if field not in data:
            return jsonify({"error":f" Missing Field {field} "}),400


    with Session(engine) as session:
        try:
            session.add(member)
            session.commit()
            session.refresh(member)
            return jsonify(member.dict()),201
        except IntegrityError:
            session.rollback()
            return jsonify({'error':'Duplicate Key Code'})


#Get all Member
@app.route('/members/list',methods=['GET'])
def get_members():
    with Session(engine) as session:
        members = session.exec(select(GymMember)).all()
    return jsonify([member.dict() for member in members])


#Get One Member
@app.route('/members/id/<int:member_id>', methods=['GET'])
def get_member(member_id):
    with Session(engine) as session:
        statement = select(GymMember).where(GymMember.id == member_id)
        member = session.exec(statement).first()  # <- get first result or None
        if member is None:
            return jsonify({"error": "Member not found"}), 404
        return jsonify(member.dict())



#Update Member
@app.route('/member/<int:member_id>',methods=['GET'])
def update_member(member_id):
    data = request.get_json()
    with Session(engine) as session:
        member = session.get(GymMember,member_id)
        if not member:
            return jsonify({'error':'Member not Found'})
        for key,value in data.items():
            setattr(member,key,value)
        session.add(member)
        session.commit()
        session.refresh(member)
    return jsonify(member.dict())

@app.route('/member/<int:member_id>',methods=['DELETE'])
def delete_member(member_id):
    with Session(engine) as session:
        member = session.get(GymMember,member_id)
        if not member:
            return jsonify({"error":"Member not found"}),404
        session.delete(member)
        session.commit()
    return jsonify({"message":"Member delete successfuly"})





if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)