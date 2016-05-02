import logging
import requests

from django.conf import settings
from urllib import parse


logger = logging.getLogger(__name__)


class Etsy(object):
    ENDPOINT = 'https://openapi.etsy.com/v2/'

    def __init__(self):
        self.api_key = settings.ETSY_API_KEY

    def request(self, method, params=None, timeout=5):
        url = self.request_url(method, params)
        logger.info('url: {}'.format(url))
        return requests.get(url, timeout=timeout).json()

    def request_url(self, method, params=None):
        url = '{endpoint}{method}?api_key={api_key}{params}'.format(
            endpoint=self.ENDPOINT,
            method=method,
            api_key=self.api_key,
            params='&{}'.format(parse.urlencode(params) if params else ''),
        )
        return url

    def get_listing_details(self, listing_id):
        return self.request('listings/{}'.format(listing_id))

    def get_listing_images(self, listing_id):
        return self.request('listings/{}/images'.format(listing_id))
