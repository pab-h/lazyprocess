from lazyprocess.services.edit import Edit as EditService
from lazyprocess.config import UPLOAD_FOLDER
from flask import request
from os import path
from uuid import uuid4 as uuid

class Edit(object):
    def __init__(self):
        self.service = EditService()

    def create(self):

        destiny = request.form.get("destiny")

        if not destiny:
            return { "message": "No destiny sent" }, 400

        image = request.files.get("image")

        if not image:
            return { "message": "No image sent" }, 400

        extension = image.filename.split(".")[-1]

        filename = f"{ uuid() }.{ extension }"

        origin = path.join(UPLOAD_FOLDER, filename)

        image.save(origin)

        self.service.create(origin, destiny)

        return { "message": "Edit queued" }
