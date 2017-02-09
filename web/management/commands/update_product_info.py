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
            data = etsy.get_listing_details(p.id)

            if not data:
                continue

            clean = self.clean_data(data)
            logger.info('data: {}\n'.format(clean))

            for k, v in clean.items():
                if v is not None and v != '':
                    setattr(p, k, v)
            p.save()

            if i % 5 == 0:
                sleep(1)

        Product.update_visibility()

    @classmethod
    def clean_data(cls, d):
        cats = d.get('category_path')
        img = d.get('MainImage', {}).get('url_170x135', '')

        entry = {
            'title': d.get('title'),
            'state': d.get('state') or 'NA',
            'price': d.get('price'),
            'currency': d.get('currency_code'),
            'tags': d.get('tags'),
            'materials': d.get('materials'),
            'style': d.get('style'),
            'taxonomy_old': cats,
            'taxonomy': d.get('taxonomy_path'),
            'category': cats[0] if cats and len(cats) > 0 else None,
            'views': d.get('views', 0),
            'favorers': d.get('num_favorers', 0),
            'image_main': img.replace('170x135', '340x270'),
            'last_synced': cls.now,
        }

        return entry
