import json
import logging

from django.core.management import BaseCommand

from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    default_filename = 'data/product-sample.json'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--filename',
            default=self.default_filename,
            help='input filename (.csv)'
        )

        parser.add_argument(
            '-a', '--append',
            dest='replace',
            action='store_false',
            default=True,
            help='Append data (default is to replace).'
        )

    def handle(self, *args, **options):
        if options['replace']:
            logger.info('erasing existing products')
            Product.objects.all().delete()

        with open(options['filename']) as f:
            data = json.load(f)

        for d in data:
            if d['state'] != 'active':
                continue

            Product.objects.create(
                id=d['listing_id'],
                title=d['title'],
                state=d['state'],
                price=d['price'],
                currency=d['currency_code'],
                category=d['taxonomy_path'],
                tags=d['tags'],
                materials=d['materials'],
                views=d['views'],
                favorers=d['num_favorers'],
                image_main=d['image']
            )
