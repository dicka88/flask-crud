from app.model.user import Users
from app.config import response

def index():
    try:
        users = Users.query.all()
        data = transform(users)

        return response.ok(data, "success")
    except Exception as e:
        return response.badRequest(null, 'failed')
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