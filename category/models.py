from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
