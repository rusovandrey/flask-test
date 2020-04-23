# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import datetime

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello_world():
    now = str(datetime.datetime.now())
    now = 'Revision 1: ' + now
    return now

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
