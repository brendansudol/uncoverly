import logging

from random import shuffle

from django.core.management import BaseCommand

from core.twitter import client
from web.models import Favorite


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        tw = client()

        faves = Favorite.objects \
            .filter(user__username='bren') \
            .filter(product__tw_featured=False) \
            .all()

        if len(faves) == 0:
            logger.info('no eligible products :(')
            return

        faves = list(faves)
        shuffle(faves)
        p = faves[0].product
        seller = p.seller.tw_handle
        hashtags = ['#etsy', '#uncoverly']

        tweet = "Today's favorite - {}{}{}".format(
            'http://www.uncoverly.com/p/{} '.format(p.pk),
            'cc: {} '.format(seller) if seller else '',
            ' '.join(hashtags)
        )

        status = tw.PostMedia(tweet, p.image_lg)
        logger.info('just posted: {}'.format(status.text))

        p.tw_featured = True
        p.save()
