from django.forms import ModelForm
from .models import Currency


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
        exclude = ['user', 'thumbnail', 'date_created']