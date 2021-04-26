from django.db import models
from django_countries.fields import CountryField
from custom_user import models as custom_user_models
from .thumbnailize import make_thumbnail


class Currency(models.Model):
    ITEM_TYPE = (
        ('Coin', 'Coin'),
        ('Banknote', 'Banknote'),
    )
    QUALITY = (
        ('Mint', 'Mint'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    )
    user = models.ForeignKey(custom_user_models.CustomUser, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=200, null=True, choices=ITEM_TYPE)
    name = models.CharField(max_length=200)
    code = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    country = CountryField(null=True)
    denomination = models.IntegerField(null=True)
    quality = models.CharField(max_length=200, null=True, choices=QUALITY)
    series = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.thumbnail = make_thumbnail(self.photo, size=(100, 100))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.name
