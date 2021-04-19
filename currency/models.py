from django.db import models
from custom_user import models as custom_user_models


class Currency(models.Model):
    ITEM_TYPE = (
        ('Coin', 'Coin'),
        ('Banknote', 'Banknote'),
    )
    user = models.ForeignKey(custom_user_models.CustomUser, null=True, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=200, null=True, choices=ITEM_TYPE)
    name = models.CharField(max_length=200, null=True)
    code = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    country = models.CharField(max_length=200, null=True)
    denomination = models.IntegerField(null=True)
    quality = models.CharField(max_length=200, null=True)
    series = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)
    test = models.CharField(max_length=200, null=True, blank=True)
    test2 = models.CharField(max_length=200, null=True, blank=True)
    test3 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.name
