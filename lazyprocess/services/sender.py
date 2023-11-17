from lazyprocess.models.edit import Edit as EditModel

class Sender(object):
    def send(self, edit: EditModel) -> bool:
        print("enviei")
        return True
