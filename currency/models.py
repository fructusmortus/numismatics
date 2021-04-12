from django.db import models

class Currency(models.Model):
    ITEM_TYPE = (
        ('Coin', 'Coin'),
        ('Banknote', 'Banknote'),
    )
    item_type = models.CharField(max_length=200, null=True, choices=ITEM_TYPE)
    name = models.CharField(max_length=200, null=True)
    code = models.IntegerField(null=True)
    release_date = models.lDateField(null=True)
    country = models.CharField(max_length=200, null=True)
    denomination = models.IntegerField(null=True)
    quality = models.CharField(max_length=200, null=True)
    series = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
