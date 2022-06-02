from flask import Flask, request
from google import googlesearch
from emploitic import emploiesearch
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route('/emploitic')
def emploie():
    return emploiesearch('djezzy')

@app.route('/search')
def searchg():
    #print(request.args)
    return googlesearch(request.args["q"])
