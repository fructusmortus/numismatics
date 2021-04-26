from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=256)
    parent_id = models.IntegerField(null=True, blank=True)
