from django.core.management import BaseCommand

from web.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.update_visibility()
