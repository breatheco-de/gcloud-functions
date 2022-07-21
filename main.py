import magic
from PIL import Image
from google.cloud import storage
from io import BytesIO
from flask import abort, jsonify, make_response
import logging
from datetime import datetime

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


def shape_of_image(request):
    data = request.get_json(force=True)

    if not 'filename' in data:
        return make_response(jsonify({'message': 'Incorrect filename', 'status_code': 400}), 400)

    if not 'bucket' in data:
        return make_response(jsonify({'message': 'Incorrect bucket', 'status_code': 400}), 400)

    bucket = data['bucket']
    filename = data['filename']

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.get_blob(filename)

    with blob.open('rb') as f:
        content = f.read()
        mime = magic.from_buffer(content, mime=True)

        if mime not in MIMES_ALLOWED:
            return make_response(jsonify({'message': 'File type not allowed', 'status_code': 400}), 400)

        image = Image.open(f)

    width, height = image.size

    if width == height:
        orientation = 'Simetrical'
        shape = 'Square'
    elif width > height:
        orientation = 'Landscape'
        shape = 'Rectangle'
    else:
        orientation = 'Portrait'
        shape = 'Rectangle'

    logger.info(f'{filename} has the shape {shape} and the orientation {orientation}')
    return make_response(jsonify({
        'shape': shape,
        'orientation': orientation,
        'status_code': 200,
        'width': width,
        'height': height,
    }), 200)

def main(request):
    starts = datetime.now()
    value = shape_of_image(request)
    ends = datetime.now()

    diff = ends - starts
    logger.info(f'Response in {diff.microseconds / 1000} ms')

    return value
