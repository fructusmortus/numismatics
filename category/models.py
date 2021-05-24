from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):

    name = models.CharField(max_length=256)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
