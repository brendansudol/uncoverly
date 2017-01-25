import json
import logging

from django.core.management import BaseCommand

from web.models import Product, Seller


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
            logger.info('erasing existing products & sellers')
            Product.objects.all().delete()
            Seller.objects.all().delete()

        with open(options['filename']) as f:
            data = json.load(f)

        for d in data:
            if d['state'] != 'active':
                continue

            seller = None
            if d['seller']:
                s = d['seller']
                seller, _ = Seller.objects.get_or_create(
                    id=s['id'],
                    defaults={'name': s['name']}
                )

            Product.objects.create(
                id=d['product_id'],
                title=d['title'],
                state=d['state'],
                price_usd=d['price_usd'],
                category=d['category'],
                tags=d['tags'],
                image_main=d['img'],
                seller=seller,
            )

        print('totals: {} products, {} sellers'.format(
            Product.objects.count(),
            Seller.objects.count(),
        ))
