from flask import Flask
from lazyprocess.routes.edit import editRoutes

app = Flask(__name__)

app.register_blueprint(editRoutes)

@app.route('/')
def hello():
    return "Hello, World!"
