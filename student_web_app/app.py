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
    return render_template('index.html')

#run the flask application
app.run(port=5001) #because 5000 taken