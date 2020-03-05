from app.model.user import Users
from app import response, app

def index():
    try:
        users = Users.query.all()
        data = transform(users)

        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(obj):
    array = []
    for i in obj:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array