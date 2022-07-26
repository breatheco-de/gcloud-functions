import random
from unittest.mock import MagicMock, patch

from src import main


class FileContent:
    def __init__(self, file):
        self.file = file

    def open(self, mode):
        return self.file


def test_without_passing_filename(build_request, to_json):
    data, status_code, headers = main(build_request())
    json = to_json(data)

    assert json == {'message': 'Incorrect filename', 'status_code': 400}
    assert status_code == 400
    assert headers == {'Content-Type': 'application/json'}


def test_without_passing_bucket(build_request, to_json, fake):
    data, status_code, headers = main(build_request({'filename': f'{fake.slug()}.{fake.file_extension()}'}))
    json = to_json(data)

    assert json == {'message': 'Incorrect bucket', 'status_code': 400}
    assert status_code == 400
    assert headers == {'Content-Type': 'application/json'}


@patch('src.utils.file.File.get_file', MagicMock(side_effect=Exception('bvc')))
def test_without_google_cloud_credentials(build_request, to_json, fake):
    data, status_code, headers = main(
        build_request({
            'filename': f'{fake.slug()}.{fake.file_extension()}',
            'bucket': fake.slug(),
        }))
    json = to_json(data)

    assert json == {'message': 'Invalid credentials', 'status_code': 500}
    assert status_code == 500
    assert headers == {'Content-Type': 'application/json'}


def test_passing_invalid_file(build_request, to_json, fake, random_file):
    file, filename = random_file()

    with patch('src.utils.file.File.get_file', MagicMock(return_value=FileContent(file))):
        data, status_code, headers = main(build_request({
            'filename': filename,
            'bucket': fake.slug(),
        }))
        json = to_json(data)

        assert json == {'message': 'File type not allowed', 'status_code': 400}
        assert status_code == 400
        assert headers == {'Content-Type': 'application/json'}


def test_passing_square_image(build_request, to_json, fake, random_image):
    n = random.randint(1, 100)
    file, filename = random_image((n, n))

    with patch('src.utils.file.File.get_file', MagicMock(return_value=FileContent(file))):
        data, status_code, headers = main(build_request({
            'filename': filename,
            'bucket': fake.slug(),
        }))
        json = to_json(data)

        assert json == {
            'height': n,
            'orientation': 'Symmetrical',
            'shape': 'Square',
            'width': n,
            'status_code': 200,
        }
        assert status_code == 200
        assert headers == {'Content-Type': 'application/json'}


def test_passing_landscape_image(build_request, to_json, fake, random_image):
    w = random.randint(1, 100)
    h = random.randint(1, w - 1)
    file, filename = random_image((w, h))

    with patch('src.utils.file.File.get_file', MagicMock(return_value=FileContent(file))):
        data, status_code, headers = main(build_request({
            'filename': filename,
            'bucket': fake.slug(),
        }))
        json = to_json(data)

        assert json == {
            'height': h,
            'orientation': 'Landscape',
            'shape': 'Rectangle',
            'width': w,
            'status_code': 200,
        }
        assert status_code == 200
        assert headers == {'Content-Type': 'application/json'}


def test_passing_portrait_image(build_request, to_json, fake, random_image):
    h = random.randint(1, 100)
    w = random.randint(1, h - 1)
    file, filename = random_image((w, h))

    with patch('src.utils.file.File.get_file', MagicMock(return_value=FileContent(file))):
        data, status_code, headers = main(build_request({
            'filename': filename,
            'bucket': fake.slug(),
        }))
        json = to_json(data)

        assert json == {
            'height': h,
            'orientation': 'Portrait',
            'shape': 'Rectangle',
            'width': w,
            'status_code': 200,
        }
        assert status_code == 200
        assert headers == {'Content-Type': 'application/json'}
