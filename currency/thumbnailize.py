from io import BytesIO
from django.core.files import File
from PIL import Image


def make_thumbnail(image, size=(100, 100)):
    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail
