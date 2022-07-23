from google.cloud import storage

__all__ = ['File']


class File:

    @staticmethod
    def get_file(bucket_name, filename):
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.get_blob(filename)
        return blob
