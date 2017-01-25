import json
import logging

from django.core.management import BaseCommand
from social_django.models import UserSocialAuth

from core.s3 import client
from web.models import Favorite, Find, Product, Seller


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--go',
            dest='go',
            action='store_true',
            default=False,
            help='Run script (deletes existing records)'
        )

        parser.add_argument(
            '-l', '--limit',
            dest='limit',
            default=1e6,
            help='Limit the number of products to backfill'
        ),

    def handle(self, *args, **options):
        s3 = client()

        if not options['go']:
            logger.info('to run, add "--go" flag (be careful!)')
            return

        # clear db

        UserSocialAuth.user_model().objects.exclude(pk='1').delete()
        UserSocialAuth.objects.all().delete()
        Product.objects.all().delete()
        Seller.objects.all().delete()
        Favorite.objects.all().delete()
        Find.objects.all().delete()

        # users

        response = s3.get('export/users.json', 'uncoverly')
        users = json.loads(response.content)

        for i, d in enumerate(users):
            fname, lname = d['first_name'] or '', d['last_name'] or ''
            uname = d['username'] or d['email'] or '{}{}'.format(fname, lname)

            user = UserSocialAuth.create_user(
                username=uname[:30],
                email=d['email'],
                first_name=fname[:30],
                last_name=lname[:30],
            )

            provider = d['provider'] or 'twitter'
            uid = d['provider_user_id'] or d['tw_user_id']

            social = UserSocialAuth.create_social_auth(
                user, uid, provider
            )

            social.extra_data = {
                'id': uid,
                'avatar': d['image_url'],
                'access_token': d['oauth_token'] or d['tw_oauth_token'],
                'old_id': d['id'],
            }
            social.save()

        logger.info('ADDED {} users, {} social users'.format(
            UserSocialAuth.user_model().objects.count(),
            UserSocialAuth.objects.count(),
        ))

        user_lookup = {}
        for su in UserSocialAuth.objects.all():
            user_lookup[su.extra_data['old_id']] = su.user.pk

        # products

        response = s3.get('export/products.json', 'uncoverly')
        data = json.loads(response.content)
        lim = int(options['limit'])

        for i, d in enumerate(data[:lim]):
            if d['state'] not in ['edit', 'sold_out', 'expired', 'active']:
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

            if i % 500 == 0:
                logger.info('done with {}...'.format(i))

        logger.info('ADDED {} products, {} sellers'.format(
            Product.objects.count(),
            Seller.objects.count(),
        ))

        db_pids = [p.pk for p in Product.objects.all()]

        # favorites

        response = s3.get('export/favorites.json', 'uncoverly')
        faves = json.loads(response.content)
        faves_clean = list(set([(f['pid'], f['uid']) for f in faves]))
        skipped = set()

        for d in faves_clean:
            pid, uid = d[0], d[1]
            if pid not in db_pids:
                skipped.add(pid)
                continue

            Favorite.objects.create(
                product_id=pid,
                user_id=user_lookup[uid],
            )

        logger.info('ADDED {} favorites ({} skipped)'.format(
            Favorite.objects.count(),
            len(skipped),
        ))

        # finds

        response = s3.get('export/finds.json', 'uncoverly')
        finds = json.loads(response.content)
        finds_clean = list(set([(f['pid'], f['uid']) for f in finds]))
        skipped.clear()

        for d in finds_clean:
            pid, uid = d[0], d[1]
            if pid not in db_pids:
                skipped.add(pid)
                continue

            Find.objects.create(
                product_id=pid,
                user_id=user_lookup[uid],
            )

        logger.info('ADDED {} finds ({} skipped)'.format(
            Find.objects.count(),
            len(skipped),
        ))
