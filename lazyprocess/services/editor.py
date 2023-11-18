from lazyprocess.models.edit import Edit as EditModel
from lazyprocess.config import UPLOAD_FOLDER
from PIL import Image
from PIL import ImageFilter
from os import path
from uuid import uuid4 as uuid

class Editor(object):

    def save(self, raw: EditModel, versions: list[Image.Image]):

        extension = raw.origin.split(".")[-1]

        for version in versions:
            filename = f"{ uuid() }.{ extension }"

            raw.versions.append(filename)
            version.save(path.join(UPLOAD_FOLDER, filename))

        filename = f"{ uuid() }.gif"
        
        versions[0].save(
            path.join(UPLOAD_FOLDER, filename), 
            save_all = True,
            append_images = versions[1::],
            duration = 1000,
            loop = 0
        )


    def apply(self, raw: EditModel) -> EditModel:

        versions: list[Image.Image] = []

        with Image.open(raw.origin) as image:
            versions.append(image.resize((500, 500)))

            versions.append(image.filter(ImageFilter.BLUR))
            versions.append(image.filter(ImageFilter.CONTOUR))
            versions.append(image.filter(ImageFilter.DETAIL))
            versions.append(image.filter(ImageFilter.EDGE_ENHANCE))
            versions.append(image.filter(ImageFilter.EDGE_ENHANCE_MORE))
            versions.append(image.filter(ImageFilter.EMBOSS))
            versions.append(image.filter(ImageFilter.FIND_EDGES))
            versions.append(image.filter(ImageFilter.SHARPEN))
            versions.append(image.filter(ImageFilter.DETAIL))
            versions.append(image.filter(ImageFilter.SMOOTH))
            versions.append(image.filter(ImageFilter.SMOOTH_MORE))

            versions.append(image.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
            versions.append(image.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
            versions.append(image.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
            versions.append(image.transpose(Image.Transpose.ROTATE_90))
            versions.append(image.transpose(Image.Transpose.ROTATE_180))
            versions.append(image.transpose(Image.Transpose.ROTATE_270))

            self.save(raw, versions)

        return raw  
    