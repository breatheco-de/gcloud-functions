#!/bin/env python
import os
import sys


if __name__ == '__main__':
    SERVICE_NAME = os.getenv('SERVICE_NAME', '')
    BUCKET_NAME = os.getenv('BUCKET_NAME', '')
    GOOGLE_CLOUD_PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID', '')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '')
    GOOGLE_CLOUD_SERVICE_ACCOUNT = os.getenv('GOOGLE_CLOUD_SERVICE_ACCOUNT', '')

    exit_code = os.system('pip freeze > requirements.txt')
    command = ' '.join([
        f'gcloud functions deploy {SERVICE_NAME}',
        '--entry-point main',
        '--runtime python39',
        '--trigger-http',
        '--memory 256MB',
        f'--service-account {GOOGLE_CLOUD_SERVICE_ACCOUNT}',
        '--source .',
        f'--project {GOOGLE_CLOUD_PROJECT_ID}',
    ])

    exit_code = os.system(command)

    # python don't return 256
    if exit_code:
        sys.exit(1)
