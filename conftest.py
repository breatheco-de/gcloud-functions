import json
import os
from unittest.mock import MagicMock
import pytest
from faker import Faker
from PIL import Image
import numpy as np
import tempfile
from scripts.utils.environment import reset_environment, test_environment

FAKE = Faker()

# set ENV as test before run django
os.environ['ENV'] = 'test'


@pytest.fixture(autouse=True)
def clean_environment():
    reset_environment()
    test_environment()


@pytest.fixture()
def build_request():
    def wrapper(data={}):
        return MagicMock(get_json=MagicMock(return_value=data), args=data)

    return wrapper


@pytest.fixture()
def random_file():
    def wrapper():
        file = tempfile.NamedTemporaryFile(suffix='.lbs', delete=False)
        file.write(os.urandom(1024))
        return file, file.name

    yield wrapper


@pytest.fixture()
def random_image(fake):

    filename = fake.slug() + '.png'

    def wrapper(size):
        image = Image.new('RGB', size)
        arr = np.random.randint(low=0, high=255, size=(size[1], size[0]))

        image = Image.fromarray(arr.astype('uint8'))
        image.save(filename, 'PNG')

        file = open(filename, 'rb')

        return file, filename

    yield wrapper

    os.remove(filename)


@pytest.fixture()
def to_json():
    def wrapper(data):
        return json.loads(data)

    return wrapper


@pytest.fixture()
def fake():
    return FAKE
