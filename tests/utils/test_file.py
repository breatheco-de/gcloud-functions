from unittest.mock import MagicMock, call, patch
from google.cloud.storage import Client, Bucket
from src.utils import File

bucket_calls = []


def bucket_mock(*args, **kwargs):
    assert isinstance(kwargs.pop('client'), Client)
    bucket_calls.append(call(*args, **kwargs))
    return None


@patch('google.cloud.storage.client.Client.__init__', MagicMock(return_value=None))
@patch('google.cloud.storage.bucket.Bucket.__init__', MagicMock(side_effect=bucket_mock))
@patch('google.cloud.storage.bucket.Bucket.get_blob', MagicMock(return_value='asdasd'))
def test_get_file(fake):
    bucket_name = fake.slug()
    filename = fake.slug()
    result = File.get_file(bucket_name, filename)

    assert result == 'asdasd'
    assert Client.__init__.call_args_list == [call()]
    assert bucket_calls == [call(name=bucket_name, user_project=None)]
    assert Bucket.get_blob.call_args_list == [call(filename)]
