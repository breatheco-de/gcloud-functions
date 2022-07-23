import logging
from datetime import datetime
import functions_framework
from src.helpers import shape_of_image

logger = logging.getLogger(__name__)

__all__ = ['main']


@functions_framework.http
def main(request):
    starts = datetime.now()
    value = shape_of_image(request)
    ends = datetime.now()

    diff = ends - starts
    logger.info(f'Response in {diff.microseconds / 1000} ms')

    return value
