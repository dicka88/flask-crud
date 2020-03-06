from app.model.user import Users
from app.config import response
from flask import request

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
        print(request)
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok([], 'Successfully create data')

    except Exception as e:
        print(e)
        print("Ini error")
        return response.ok([], 'Successfully create data')