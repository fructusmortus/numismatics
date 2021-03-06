from django import forms
from .models import Currency
from category.models import Category
from .utils import categories_to_dropdown_options
from mptt.forms import TreeNodeChoiceField


class DateInput(forms.DateInput):
    input = 'date'


class CurrencyForm(forms.ModelForm):
    release_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    category = TreeNodeChoiceField(queryset=Category.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Currency
        fields = '__all__'
        exclude = ['user', 'thumbnail', 'date_created']

        widgets = {
            'item_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'denomination': forms.TextInput(attrs={'class': 'form-control'}),
            'quality': forms.Select(attrs={'class': 'form-control'}),
            'series': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
