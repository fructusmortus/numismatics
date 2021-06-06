from django.db import models
from custom_user.models import CustomUser
from currency.models import Currency


class Collection(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    currencies = models.ManyToManyField(Currency)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
