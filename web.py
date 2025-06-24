import flask
#flask is a server
from flask import request,jsonify

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

# create 2 routes

# 1 route - return all student data
# 1 route - return students by major

# run the application
app.run()
