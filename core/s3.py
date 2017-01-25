import tinys3

from django.conf import settings


def client():
    return tinys3.Connection(settings.S3_ACCESS_KEY, settings.S3_SECRET_KEY)
