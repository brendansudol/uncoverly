import json
import logging

from time import sleep
from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        etsy = Etsy()

        products = Product.objects \
            .order_by('updated')

        logger.info('total products: {}'.format(len(products)))

        for i, p in enumerate(products[:5]):
            data = etsy.get_listing_details(p.id)

            if not data:
                continue

            data_cleaned = self.clean_data(data)
            logger.info('data: {}\n'.format(data_cleaned))

            for k, v in data_cleaned.items():
                setattr(p, k, v)
            p.save()

            if i % 5 == 0:
                sleep(1)

    @classmethod
    def clean_data(cls, d):
        cats = d.get('category_path', [])
        img = d.get('MainImage', {}).get('url_170x135', '')

        entry = {
            'title': d.get('title'),
            'state': d.get('state'),
            'price': d.get('price'),
            'currency': d.get('currency_code'),
            'category': cats[0] if len(cats) > 0 else None,
            'tags': json.dumps(d.get('tags')),
            'materials': json.dumps(d.get('materials')),
            'views': d.get('views', 0),
            'favorers': d.get('num_favorers', 0),
            'image_main': img.replace('170x135', '340x270'),
        }

        return entry
