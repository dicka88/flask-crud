from app import app
from app.controller import mainController

@app.route('/')
@app.route('/index')
def index():
    return mainController.index()