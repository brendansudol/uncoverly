from collections import defaultdict
from datetime import datetime
from functools import reduce
from operator import or_
from random import randrange, shuffle

from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models import Q
from jsonfield import JSONField


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

    def __str__(self):
        return self.id


class ProductManager(models.Manager):
    def search(self, terms):
        terms = [term.strip() for term in terms.split()]

        q_objs = []
        for term in terms:
            q_objs.append(Q(title__icontains=term))
            q_objs.append(Q(tags__icontains=term))

        qs = self.get_queryset()
        return qs.filter(reduce(or_, q_objs))

    def is_active(self, val=True):
        qs = self.get_queryset()

        if not val:
            return qs.exclude(state='active')

        return qs.filter(state='active')


class Product(ModelBase):
    def rand_default():
        return randrange(1e4)

    id = models.CharField(max_length=64, primary_key=True)
    seller = models.ForeignKey(
        Seller, related_name='products', null=True, blank=True
    )
    title = models.CharField(max_length=1024, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    price = models.CharField(max_length=32, null=True, blank=True)
    currency = models.CharField(max_length=32, null=True, blank=True)
    price_usd = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=512, null=True, blank=True)
    tags = models.CharField(max_length=512, null=True, blank=True)
    materials = models.CharField(max_length=512, null=True, blank=True)
    views = models.PositiveIntegerField(null=True, blank=True)
    favorers = models.PositiveIntegerField(null=True, blank=True)
    image_main = models.URLField(null=True, blank=True)
    is_awesome = models.NullBooleanField()
    is_visible = models.BooleanField(default=False)
    last_synced = models.DateTimeField(default=datetime.now, blank=True)
    rand1 = models.PositiveIntegerField(default=rand_default)
    rand2 = models.PositiveIntegerField(default=rand_default)

    objects = ProductManager()

    def __str__(self):
        return self.id

    @property
    def image_lg(self):
        if self.image_main:
            return self.image_main.replace("340x270", "570xN")

    @property
    def price_display(self):
        if self.price_usd:
            return '${}'.format(round(self.price_usd / 100.0))

    @property
    def is_eligible(self):
        return bool(
            self.state == 'active' and
            self.is_awesome and
            all([self.title, self.price_usd, self.image_main])
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
