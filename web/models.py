from collections import defaultdict, OrderedDict
from functools import reduce
from operator import or_
from random import randrange, shuffle

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models, transaction
from django.db.models import Q
from django.utils import timezone
from jsonfield import JSONField


def rand_int():
    return randrange(1e4)


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Seller(ModelBase):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=1024, null=True, blank=True)
    icon_url = models.URLField(null=True, blank=True)
    num_favorers = models.PositiveIntegerField(null=True, blank=True)
    listings_all_count = models.PositiveIntegerField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    social = JSONField(null=True, blank=True)

    visible_product_count = models.IntegerField(null=True, blank=True)

    rand = models.PositiveIntegerField(default=rand_int)

    def __str__(self):
        return self.id

    @property
    def active_products(self):
        return self.products.filter(is_visible=True)

    @property
    def tw_handle(self):
        tw = (self.social or {}).get('twitter')

        if not tw:
            return

        return '@{}'.format(tw.split('/')[-1])

    @classmethod
    def update_product_count(cls):
        for s in cls.objects.prefetch_related('products'):
            ct = len([p for p in s.products.all() if p.is_visible])
            s.visible_product_count = ct
            s.save()

    @classmethod
    def randomize(cls):
        sellers = cls.objects.all()
        nums = list(range(len(sellers)))
        shuffle(nums)
        with transaction.atomic():
            for i, s in enumerate(sellers):
                s.rand = nums[i]
                s.save()


class ProductManager(models.Manager):
    def search(self, q):
        q_objs = [
            Q(title__icontains=q),
            Q(taxonomy__contains=[q]),
            Q(style__contains=[q]),
            Q(materials__contains=[q]),
        ]

        qs = self.get_queryset()
        return qs.filter(reduce(or_, q_objs))

    def is_active(self, val=True):
        qs = self.get_queryset()

        if not val:
            return qs.exclude(state='active')

        return qs.filter(state='active')

    def color_search(self, hex, dist=20):
        rgb = list(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        r, g, b = [(max(0, c - dist), min(255, c + dist)) for c in rgb]

        qs = self.get_queryset().filter(imagedetail__isnull=False)

        return qs \
            .filter(imagedetail__red__gte=r[0], imagedetail__red__lte=r[1]) \
            .filter(imagedetail__green__gte=g[0], imagedetail__green__lte=g[1]) \
            .filter(imagedetail__blue__gte=b[0], imagedetail__blue__lte=b[1])


class Product(ModelBase):
    id = models.CharField(max_length=64, primary_key=True)
    seller = models.ForeignKey(
        Seller, related_name='products', null=True, blank=True
    )

    title = models.CharField(max_length=1024, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)

    price = models.CharField(max_length=32, null=True, blank=True)
    currency = models.CharField(max_length=32, null=True, blank=True)
    price_usd = models.PositiveIntegerField(null=True, blank=True)

    tags = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    materials = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    style = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    taxonomy_old = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    taxonomy = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    views = models.PositiveIntegerField(null=True, blank=True)
    favorers = models.PositiveIntegerField(null=True, blank=True)

    image = models.URLField(null=True, blank=True)

    last_synced = models.DateTimeField(default=timezone.now, blank=True)

    is_awesome = models.NullBooleanField()
    is_visible = models.BooleanField(default=False)
    tw_featured = models.BooleanField(default=False)

    rand1 = models.PositiveIntegerField(default=rand_int)
    rand2 = models.PositiveIntegerField(default=rand_int)

    objects = ProductManager()

    def __str__(self):
        return self.id

    @property
    def category(self):
        tax = self.taxonomy
        return tax[0] if tax else None

    @property
    def keywords(self):
        data = [self.taxonomy, self.style, self.materials]
        words = [i for d in data if d is not None for i in d]
        return list(OrderedDict.fromkeys(words))

    @property
    def image_lg(self):
        if self.image:
            return self.image.replace("340x270", "570xN")

    @property
    def price_display(self):
        if self.price_usd:
            return '${}'.format(round(self.price_usd / 100.0))

    @property
    def is_eligible(self):
        return bool(
            self.state == 'active' and
            self.is_awesome and
            all([self.title, self.price_usd, self.image])
        )

    @classmethod
    def update_visibility(cls):
        results = defaultdict(int)
        for p in cls.objects.all():
            e, v = p.is_eligible, p.is_visible
            if e == v:
                continue
            p.is_visible = e
            p.save()
            results['now {}'.format('visible' if e else 'hidden')] += 1
        print(dict(results))

    @classmethod
    def randomize(cls):
        products = cls.objects.all()
        nums1 = list(range(len(products)))
        nums2 = list(nums1)
        shuffle(nums1)
        shuffle(nums2)
        with transaction.atomic():
            for i, p in enumerate(products):
                p.rand1 = nums1[i]
                p.rand2 = nums2[i]
                p.save()


class ImageDetail(ModelBase):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    id = models.CharField(max_length=32)
    hex_code = models.CharField(max_length=16, null=True, blank=True)
    red = models.PositiveIntegerField(null=True, blank=True)
    green = models.PositiveIntegerField(null=True, blank=True)
    blue = models.PositiveIntegerField(null=True, blank=True)
    hue = models.PositiveIntegerField(null=True, blank=True)
    saturation = models.PositiveIntegerField(null=True, blank=True)
    brightness = models.PositiveIntegerField(null=True, blank=True)
    full_height = models.PositiveIntegerField(null=True, blank=True)
    full_width = models.PositiveIntegerField(null=True, blank=True)
    square_url = models.URLField(null=True, blank=True)


class Favorite(ModelBase):
    product = models.ForeignKey(Product, related_name='favorites')
    user = models.ForeignKey(User, related_name='favorites')

    class Meta:
        unique_together = ('product', 'user')


class Find(ModelBase):
    product = models.ForeignKey(Product, related_name='finds')
    user = models.ForeignKey(User, related_name='finds')

    class Meta:
        unique_together = ('product', 'user')


# add method(s) to User class
class UserFunctions:
    @property
    def avatar(self):
        social = self.social_auth.first()

        if not social:
            return

        return social.extra_data.get('avatar')

User.__bases__ += (UserFunctions,)
