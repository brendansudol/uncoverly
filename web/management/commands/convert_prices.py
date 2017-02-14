import logging

from django.core.management import BaseCommand

from core.currency import Currency
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        latest_rates = Currency()
        products = Product.objects.all()
        skip = update = error = 0

        for i, p in enumerate(products):
            if not p.price or not p.currency:
                skip += 1
                continue

            try:
                cents_local = int(float(p.price) * 100)
                p.price_usd = latest_rates.to_usd(cents_local, p.currency)
                p.save()
                update += 1
            except Exception as e:
                logger.warn('error: {}'.format(str(e)))
                error += 1

        logger.info('s: {}, u: {}, e: {}'.format(skip, update, error))
