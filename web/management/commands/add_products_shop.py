import logging

from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    MAX_PAGE = 3

    def add_arguments(self, parser):
        parser.add_argument(
            '--shop',
            dest='shop',
            default='6359201',
        )

    def handle(self, *args, **options):
        shop = options['shop']
        results, page, skips = [], 1, 0
        etsy = Etsy()

        while page is not None and page <= self.MAX_PAGE:
            data = etsy.get_shop_listings(shop, page)
            results += data['results']
            page = data['pagination']['next_page']

        logger.info('eligible products: {}'.format(len(results)))

        for r in results:
            pid = r['listing_id']
            img = r['MainImage']['url_170x135'].replace('170x135', '340x270')

            if Product.objects.filter(pk=pid).first():
                skips += 1
                continue

            Product.objects.create(id=pid, image=img)

        logger.info('added: {}; skipped: {}'.format(len(results) - skips, skips))
