from flask.blueprints import Blueprint
from lazyprocess.controllers.edit import Edit as EditController

editRoutes = Blueprint("edit", __name__, url_prefix='/edit')

controller = EditController()

@editRoutes.post("/create")
def create():
    return controller.create()
