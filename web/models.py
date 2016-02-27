from django.db import models


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class Foo(ModelBase):
#     foo = models.DateField(db_index=True)
#     bar = models.CharField(max_length=256)
#     baz = models.PositiveIntegerField(blank=True, null=True)
