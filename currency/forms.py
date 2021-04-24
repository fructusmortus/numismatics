from django import forms
from .models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
        exclude = ['user', 'thumbnail', 'date_created']
        
        widgets = {
                'item_type' : forms.Select(attrs={'class': 'form-control'}),
                'name' : forms.TextInput(attrs={'class': 'form-control'}),
                'code' : forms.TextInput(attrs={'class': 'form-control'}),
                'country': forms.TextInput(attrs={'class': 'form-control'}),
                'release_date': forms.TextInput(attrs={'class': 'form-control'}),
                'denomination': forms.TextInput(attrs={'class': 'form-control'}),
                'quality': forms.Select(attrs={'class': 'form-control'}),
                'series': forms.TextInput(attrs={'class': 'form-control'}),
                'photo': forms.FileInput(attrs={'class': 'form-control'}),
            }