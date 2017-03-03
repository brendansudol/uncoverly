from django.core.management import BaseCommand
from django.utils import timezone

from web.models import Product, Seller


class Command(BaseCommand):
    now = timezone.now()

    def handle(self, *args, **options):
        Product.randomize()

        if self.now.hour == 12:
            Seller.randomize()
