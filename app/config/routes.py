from app import app
from app.controller import mainController
from app.controller import todoController
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
    
@app.route('/login', methods=['POST'])
def login():
    return mainController.login()

@app.route('/todo', methods=['POST', 'GET'])
def todo():
    if request.method == 'GET':
        return todoController.index()
    else:
        return todoController.store()

@app.route('/todo/<id>', methods=['PUT', 'GET', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return todoController.show(id)
    elif request.method == 'PUT':
        return todoController.update(id)
    elif request.method == 'DELETE':
        return todoController.delete(id)

@app.route('/refresh', methods=['POST'])
def refresh():
    return mainController.refresh()
