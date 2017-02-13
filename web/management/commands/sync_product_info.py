import logging

from datetime import timedelta
from time import sleep

from django.core.management import BaseCommand
from django.utils import timezone

from core.etsy import Etsy
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    now = timezone.now()
    limit = 2000

    def add_arguments(self, parser):
        parser.add_argument(
            '--inactive',
            dest='inactive',
            action='store_true',
            default=False,
            help='Update inactive products'
        )

        parser.add_argument(
            '--mode',
            dest='mode',
            default='adhoc',
        )

    def handle(self, *args, **options):
        mode = options['mode']
        is_active = not options['inactive']
        etsy = Etsy()

        if mode == 'hourly':
            hour = self.now.hour
            is_active = False if hour == 0 else is_active
            if hour % 4 != 0:
                logger.info('skipping run (hour is {})'.format(hour))
                return

        products = Product.objects \
            .is_active(is_active) \
            .filter(last_synced__lt=self.now - timedelta(days=2)) \
            .order_by('last_synced')

        logger.info('total products: {}'.format(len(products)))

        for i, p in enumerate(products[:self.limit]):
            data = etsy.get_listing(p.id)

            if not data:
                continue

            clean = etsy.parse_listing(data)
            logger.info('data: {}\n'.format(clean))

            for k, v in clean.items():
                if v is None or v == '' or k == 'seller_id':  # TODO - clean up
                    continue
                setattr(p, k, v)
            p.save()

            if i % 5 == 0:
                sleep(1)

        Product.update_visibility()
