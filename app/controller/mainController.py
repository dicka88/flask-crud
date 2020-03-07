from app.model.user import Users
from app.config import response

from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import Flask
from app import db

def index():
    try:
        users = Users.query.all()
        data = _transform(users)
        return response.ok(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest([], 'failed')

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty..')
        data = _singleTransform(users)
        return response.ok(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest([], 'failed')

def _transform(obj):
    array = []
    for i in obj:
        array.append(_singleTransform(i))
    return array

def _singleTransform(obj):
    return {
        'id': obj.id,
        'name': obj.name,
        'email': obj.email
    }

def store():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok([], 'Successfully create data')

    except Exception as e:
        print(e)
        return response.ok([], 'Failed, user is exist')

def update(id):
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(id=id).first()
        user.email = email
        user.name = name
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Successfully update data!')
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Users didn\' found')
        
        db.session.delete(user)
        db.session.commit()

        return response.ok([], 'Successfully delete')
    except Exception as e:
        print(e)

def login():
    try:
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], 'Empty...')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Password is wrong')
        
        data = _singleTransform(user)
        return response.ok(data, 'Success signin')

    except Exception as e:
        print(e)
        return response.badRequest([], 'Params is failed')