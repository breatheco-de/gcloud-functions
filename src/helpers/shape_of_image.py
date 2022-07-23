import magic
from PIL import Image
import logging

from src import utils
from src.helpers.response import response

logger = logging.getLogger(__name__)

# you can add new mimes from here https://www.sitepoint.com/mime-types-complete-list/
# name of formats https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
MIMES_ALLOWED = {
    # 'mime': 'format',
    'image/gif': 'gif',
    'image/x-icon': 'ico',
    'image/jpeg': 'jpeg',
    # 'image/svg+xml': 'svg', not have sense resize a svg
    # 'image/tiff': 'tiff', don't work
    'image/webp': 'webp',
    'image/png': 'png',
}

__all__ = ['shape_of_image']

from flask.wrappers import Request


def shape_of_image(request: Request):
    data = request.get_json(force=True)

    if not 'filename' in data:
        return response({'message': 'Incorrect filename', 'status_code': 400}, status_code=400)

    if not 'bucket' in data:
        return response({'message': 'Incorrect bucket', 'status_code': 400}, status_code=400)

    bucket = data['bucket']
    filename = data['filename']

    try:
        blob = utils.File.get_file(bucket, filename)
    except:
        return response({'message': 'Invalid credentials', 'status_code': 500}, status_code=500)

    with blob.open('rb') as f:

        content = f.read()
        mime = magic.from_buffer(content, mime=True)

        if mime not in MIMES_ALLOWED:
            return response({'message': 'File type not allowed', 'status_code': 400}, status_code=400)

        image = Image.open(f)

    width, height = image.size

    if width == height:
        orientation = 'Symmetrical'
        shape = 'Square'
    elif width > height:
        orientation = 'Landscape'
        shape = 'Rectangle'
    else:
        orientation = 'Portrait'
        shape = 'Rectangle'

    logger.info(f'{filename} has the shape {shape} and the orientation {orientation}')
    return response(
        {
            'shape': shape,
            'orientation': orientation,
            'status_code': 200,
            'width': width,
            'height': height,
        },
        status_code=200)
