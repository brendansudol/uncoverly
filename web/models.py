from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return self.id


class Favorite(ModelBase):
    product = models.ForeignKey(Product, related_name='favorites')
    user = models.ForeignKey(User, related_name='favorites')

    class Meta:
        unique_together = ('product', 'user')
