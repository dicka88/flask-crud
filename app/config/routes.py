from app import app
from app.controller import mainController
from flask import request

@app.route('/')
def home():
    return "Hello world"

@app.route('/user')
def index():
    return mainController.index()

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def userDetail(id):
    if(request.method == 'GET'):
        return mainController.show(id)
    elif(request.method == 'PUT'):
        return mainController.update(id)
    elif(request.method == 'DELETE'):
        return mainController.delete(id)

@app.route('/user', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return mainController.index()
    else:
        return mainController.store()

