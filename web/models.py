from functools import reduce
from operator import or_
from random import randrange

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


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


class Product(ModelBase):
    id = models.CharField(max_length=64, primary_key=True)
    seller = models.ForeignKey(
        Seller, related_name='products', null=True, blank=True
    )
    title = models.CharField(max_length=1024, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    price = models.CharField(max_length=32, null=True, blank=True)
    currency = models.CharField(max_length=32, null=True, blank=True)
    category = models.CharField(max_length=512, null=True, blank=True)
    tags = models.CharField(max_length=512, null=True, blank=True)
    materials = models.CharField(max_length=512, null=True, blank=True)
    views = models.PositiveIntegerField(null=True, blank=True)
    favorers = models.PositiveIntegerField(null=True, blank=True)
    image_main = models.URLField(null=True, blank=True)
    is_awesome = models.NullBooleanField()
    is_visible = models.BooleanField(default=False)
    rand1 = models.PositiveIntegerField(default=randrange(1e4))

    objects = ProductManager()

    def __str__(self):
        return self.id


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
