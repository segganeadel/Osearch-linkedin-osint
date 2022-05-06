from flask import Flask
from emploitic import emploiesearch
from google import search
app = Flask(__name__)

@app.route('/emploitic')
def emploie():
    return emploiesearch('djezzy')

@app.route('/google')
def searchg():
    return search('djezzy')
