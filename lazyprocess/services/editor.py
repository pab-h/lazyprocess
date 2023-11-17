from lazyprocess.models.edit import Edit as EditModel

class Editor(object):
    def apply(self, raw: EditModel) -> EditModel:
        print("edicao pica das galaxisas")
        return raw