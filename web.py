import flask
#flask is a server
from flask import request,jsonify
import student_generator_v2 as sg

# create a flask app object

app = flask.Flask(__name__)

# tell the server to reload each time the code
app.config["DEBUG"] = True
#debug allows for changes to happen while the server is running instead of manually reloading

# load student dictionaries



#create a route to display the names
@app.route('/',methods=['GET'])
def index():
    return "<h1> My name is Osvin Alaphat </h1>"

#create a route to return all student data
@app.route('/api/students/all',methods=['GET'])
def api_all():
    #load student dictionaries
    student_dictionaries = sg.get_student_dictionary()
    return jsonify(student_dictionaries)

#create a rpite tp return students by major
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major):
    print(major)
    #get students with that major
    #get all students
    student_dictionaries = sg.get_student_dictionary()
    major_students = []

    for student in student_dictionaries:
        if major.lower() == student['major'].lower():
            major_students.append(student)
    return jsonify(major_students)


# create 2 routes

# 1 route - return all student data  
# 1 route - return students by major

# run the application
app.run()
#
