import logging
import requests


logger = logging.getLogger(__name__)


class Currency(object):
    URL = 'http://api.fixer.io/latest?base=USD'

    def __init__(self):
        self.rates = self.fetch_rates()

    def fetch_rates(self):
        try:
            response = requests.get(self.URL).json()
            logger.info('api response: {}'.format(response))
            return response['rates']
        except Exception as e:
            logger.warn('error fetching rates: {}'.format(str(e)))

    def to_usd(self, from_cents, from_curr):
        if not self.rates:
            raise ValueError('no rate data')

        if not isinstance(from_cents, int):
            raise ValueError('non-int amount')

        if not from_curr:
            raise ValueError('no currency')

        from_curr = from_curr.upper()
        if from_curr == 'USD':
            return from_cents

        if from_curr not in self.rates:
            raise ValueError('unsupported currency')

        usd = float(from_cents) * (1 / self.rates[from_curr])
        return int(round(usd))
