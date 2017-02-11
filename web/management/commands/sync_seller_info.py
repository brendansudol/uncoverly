import logging

from time import sleep
from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import Seller


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-l', '--limit',
            dest='limit',
            default=2000,
        ),

    def handle(self, *args, **options):
        limit = int(options['limit'])
        etsy = Etsy()

        sellers = Seller.objects \
            .filter(title__isnull=True) \
            .order_by('updated')

        logger.info('total shops: {}'.format(len(sellers)))

        for i, s in enumerate(sellers[:limit]):
            logger.info('{}...\n'.format(s.id))
            data = etsy.get_shop(s.id)

            if not data:
                continue

            clean = etsy.parse_shop(data)
            logger.info('data: {}\n'.format(clean))

            for k, v in clean.items():
                setattr(s, k, v)
            s.save()

            if i % 5 == 0:
                sleep(1)
