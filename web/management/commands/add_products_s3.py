import json
import logging

from django.core.management import BaseCommand

from core.s3 import client
from web.models import Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', dest='path')

    def handle(self, *args, **options):
        if not options['path']:
            logger.info('specify a "path" please!')
            return

        s3 = client()
        skips = 0

        response = s3.get(options['path'], 'uncoverly')
        data = json.loads(response.content)

        logger.info('eligible products: {}'.format(len(data)))

        for d in data:
            pid = int(d['id'])

            if Product.objects.filter(pk=pid).first():
                skips += 1
                continue

            Product.objects.create(id=pid, image=d.get('img'))

        logger.info('added: {}; skipped: {}'.format(len(data) - skips, skips))
