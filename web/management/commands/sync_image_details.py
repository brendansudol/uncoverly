import logging

from time import sleep
from django.core.management import BaseCommand

from core.etsy import Etsy
from web.models import ImageDetail, Product


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    limit = 1000

    def handle(self, *args, **options):
        etsy = Etsy()

        products = Product.objects \
            .filter(is_visible=True) \
            .filter(imagedetail__isnull=True) \
            .all()

        logger.info('total products: {}'.format(len(products)))

        for i, p in enumerate(products[:self.limit]):
            data = etsy.get_listing_images(p.id)

            if not data:
                continue

            results = data.get('results') or [data]  # in case of only 1 img
            main_img_info, = [r for r in results if r['rank'] == 1]

            clean = self.clean_data(main_img_info)
            logger.info('data: {}\n'.format(clean))

            main_url = clean['square_url'].replace('75x75', '340x270')
            if main_url != p.image:
                p.image = main_url
                p.save()

            ImageDetail.objects.update_or_create(product=p, defaults=clean)

            if i % 5 == 0:
                sleep(1)

    def clean_data(self, d):
        fields = [
            'hex_code', 'red', 'green', 'blue', 'hue',
            'saturation', 'brightness', 'full_height', 'full_width'
        ]

        cleaned = {k: v for k, v in d.items() if k in fields}
        cleaned.update({
            'id': d['listing_image_id'],
            'square_url': d['url_75x75']
        })

        return cleaned
