from flask import Flask, request
from emploitic import emploiesearch
from flask_cors import CORS
from searx import searchpass
from company import Company


app = Flask(__name__)

CORS(app)


@app.route('/search')
def search():
    return searchpass(request.args["q"])

@app.route('/company')
def emploie():
    return Company(request.args["q"])
