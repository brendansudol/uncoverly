import logging

from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    MAX_PAGE = 3

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            dest='username',
            default='brendan14701',
        )

    def handle(self, *args, **options):
        name = options['username']
        faves, page, skips = [], 1, 0
        etsy = Etsy()

        while page is not None and page <= self.MAX_PAGE:
            data = etsy.get_user_faves(name, page)
            faves += data['results']
            page = data['pagination']['next_page']

        faves = [f for f in faves if f['listing_state'] == 'active']
        logger.info('eligible products: {}'.format(len(faves)))

        for f in faves:
            pid = f['listing_id']

            if Product.objects.filter(pk=pid).first():
                skips += 1
                continue

            data = etsy.get_listing(pid)
            clean = etsy.parse_listing(data)
            Product.objects.create(id=pid, image_main=clean['image_main'])

        logger.info('added: {}; skipped: {}'.format(len(faves) - skips, skips))
