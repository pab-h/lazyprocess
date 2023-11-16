from lazyprocess.models.edit import Edit as EditModel

class Edit(object):
    def create(self, origin: str, destiny: str) -> EditModel:
        return EditModel(origin, destiny, [])
