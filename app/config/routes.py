from app import app
from app.controller import mainController
from flask import request

@app.route('/')
def home():
    return "Hello world"

@app.route('/user')
def index():
    return mainController.index()

@app.route('/user/<id>')
def userDetail(id):
    print(id)
    return mainController.show(id)

@app.route('/user', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return mainController.index()
    else:
        return mainController.store()

