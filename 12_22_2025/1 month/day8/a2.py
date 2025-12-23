from flask import Flask,request,jsonify
import json
import pandas as pd

app = Flask(__name__)

with open('student.json','r') as file:
    student = json.load(file)

@app.route('/student',methods=['GET'])
def get_student():
    return jsonify(student),200

@app.route('/student/id/<int:id>',methods=['GET'])
def get_student_id(id):
     
    with open('student.json','r') as file:
        students = json.load(file)

    student = next((u for u in students if u['id'] == id),None)
    if not student:
        return jsonify({'error':'Student not Found'}),404
   
        
    return jsonify({'student':student})

@app.route('/student/name/<string:name>',methods=['GET'])
def get_student_name(name):

    with open('student.json','r') as file:
        students = json.load(file)
    
    student = [u for u in students if u['name'].lower().startswith(name.lower())]
    if not student:
        return jsonify({"error":'Student not Found'}),404
    
    return jsonify({'student':student}),200


@app.route('/student/subject/<string:subject>',methods=['GET'])
def get_student_subject(subject):
    
    with open('student.json','r') as file:
        students = json.load(file)
    
    matched_students = [
        s for s in students 
        if any(subj.lower() == subject.lower() for subj in s['subjects'])
    ]

    if not matched_students:
        return jsonify({'error':'Subject not  found'}),404
    
    return jsonify({'subject':matched_students}),200


@app.route('/student/count',methods=['GET'])
def get_student_count():

    with open('student.json','r') as file:
        students = json.load(file)

    count = len(students)

    return jsonify({'message':f'There are {count} students'}),200

#Get the number of students per subject.
@app.route('/student/count/subject',methods=['GET'])
def get_subject_count():

    with open('student.json','r') as file:
        data = json.load(file)


    subject_count = {}

    for student in data:
        for subject in student['subjects']:
            if subject in subject_count:
                subject_count[subject] += 1
            else:
                subject_count[subject] = 1

    return jsonify(subject_count)

#Return the average age of students.
@app.route('/student/count/age/average',methods=['GET'])
def get_average_age():
    
    with open('student.json','r') as file:
        data = json.load(file)
    
    

    ages = [student['age'] for student in data]
    
    average = pd.Series(ages).mean()

    return jsonify({"average":round(average,1)})

if __name__ == '__main__':
    app.run(debug=True)