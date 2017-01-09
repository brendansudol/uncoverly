import logging

from time import sleep
from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import Seller


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        etsy = Etsy()

        sellers = Seller.objects \
            .filter(title__isnull=True) \
            .order_by('updated')

        logger.info('total shops: {}'.format(len(sellers)))

        for i, s in enumerate(sellers[:100]):
            logger.info('{}...\n'.format(s.id))
            data = etsy.get_shop_info_all(s.id)

            if not data:
                continue

            data_cleaned = self.clean_data(data)
            for k, v in data_cleaned.items():
                setattr(s, k, v)
            s.save()

            if i % 5 == 0:
                sleep(1)

    @classmethod
    def clean_data(cls, d):
        story, social = None, None
        if d['more']:
            story = d['more']['story']
            links = d['more'].get('related_links', {})
            social = {
                l['title']: l['url']
                for l in (links.values() if type(links) == dict else links)
            }

        entry = {
            'name': d['shop_name'],
            'title': d['title'],
            'icon_url': d['icon_url_fullxfull'],
            'num_favorers': d.get('num_favorers', 0),
            'listings_all_count': d['listing_active_count'],
            'story': story,
            'social': social or None,
        }

        return entry
