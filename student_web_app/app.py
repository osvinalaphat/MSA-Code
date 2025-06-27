from flask import Flask,render_template,request,url_for,redirect,abort,flash
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the API
Input: url
Output: JSON student data
"""
def get_student_data(url:str):
    #make a request
    response = requests.get(url)

    # convert the response format to JSON
    response_json = response.json() 
    return response_json

    #create a route for the website index/root. Will display all the student data
@app.route('/',methods=['GET'])
def index():
    #make a request to the student API
    url = 'http://127.0.0.1:5000/api/students/all'

    #get the student data
    student_data = get_student_data(url)
    
    return render_template('index.html', student_data=student_data)

#create a route for the majors search page with GET requests
@app.route('/majors',methods=['GET'])
def majors_get():
    #get list of student data
    #twooooooooooooooooooooooooooooooooooooooooooooooo driftyerrrrrrrrssss offf to tseee the worldddddddddddd its sucha crazy world youll seeeee we're allllllllllllllllllllllllllllllllllllllllllllllllllllllll chasing aftert
    # our endssss chsaing after our endddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddds 
    url = "http://127.0.0.1:5000/api/students/all"
    student_data = get_student_data(url)
   
    # create a list to store unique majors
    major_list = []
    # use for loop to iterate through the student list
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])
    # add major to majors list if major not currently in list
    major_list.sort()
        #get the form data: chosen major
        # create the request url to get students with that major
        # send the request and get the response
        # send the results to the majors template 
    

    return render_template('majors.html', major_list = major_list)

#create a route for the majors search page with GET requests
@app.route('/majors',methods=['POST'])
def majors_post():
    #get list of student data
    #twooooooooooooooooooooooooooooooooooooooooooooooo driftyerrrrrrrrssss offf to tseee the worldddddddddddd its sucha crazy world youll seeeee we're allllllllllllllllllllllllllllllllllllllllllllllllllllllll chasing aftert 
    url = "http://127.0.0.1:5000/api/students/all"
    student_data = get_student_data(url)
   
    # create a list to store unique majors
    major_list = []
    # use for loop to iterate through the student list
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])
    # add major to majors list if major not currently in list
    major_list.sort()
        #get the form data: chosen major
        # create the request url to get students with that major
        # send the request and get the response
        # send the results to the majors template 
    major = request.form.get('major')
    print(major)
    
    url = f"http://127.0.0.1:5000/api/majors/{major}"

    result_list = get_student_data(url)
    
    return render_template('majors.html',major_list=major_list,result_list=result_list)

#run the flask application
app.run(port=5001) #because 5000 taken 