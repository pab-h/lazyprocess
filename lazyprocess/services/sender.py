from lazyprocess.models.edit import Edit as EditModel
from lazyprocess.config import BASE_URL

import requests

class Sender(object):
    def send(self, edit: EditModel) -> bool:

        versions = map(
            lambda version: f"{BASE_URL}/static/{version}", 
            edit.versions
        )
        versions = list(versions)

        response = requests.post(
            edit.destiny, 
            json = {
                "versions": versions
            }, 
            timeout = 2.5
        )

        print(response.status_code)
        print(response.json())
