from flask import Flask
from lazyprocess.routes.edit import editRoutes
from lazyprocess.config import UPLOAD_FOLDER

app = Flask(__name__)

app.static_folder = UPLOAD_FOLDER

app.register_blueprint(editRoutes)

@app.route('/')
def hello():
    return "Hello, World!"
