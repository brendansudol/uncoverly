import logging
import requests

from django.conf import settings
from urllib import parse


logger = logging.getLogger(__name__)


class Etsy(object):
    ENDPOINT = 'https://openapi.etsy.com/v2/'

    def __init__(self):
        self.api_key = settings.ETSY_API_KEY

    def request_url(self, method, params=None):
        url = '{endpoint}{method}?api_key={api_key}{params}'.format(
            endpoint=self.ENDPOINT,
            method=method,
            api_key=self.api_key,
            params='&{}'.format(parse.urlencode(params) if params else ''),
        )
        return url

    def get(self, method, params=None, timeout=5):
        url = self.request_url(method, params)
        logger.info('url: {}'.format(url))
        res = requests.get(url, timeout=timeout)

        if res.status_code != 200:
            logger.warn('uh-oh! status: {}, reason: {}'.format(
                res.status_code, res.text
            ))
            return

        data = res.json()
        return None if not data else data['results'][0]

    def get_listing_details(self, listing_id):
        return self.get(
            'listings/{}'.format(listing_id),
            {'includes': 'MainImage,Shop'}
        )

    def get_shop_info(self, shop_id):
        path = 'shops/{}'.format(shop_id)
        data = self.get(path)

        if not data:
            return

        data['more'] = self.get('{}/about'.format(path))
        return data
