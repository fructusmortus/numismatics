from django import forms
from .models import Collection
from currency.models import Currency


class SaveCollectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SaveCollectionForm, self).__init__(*args, **kwargs)
        self.fields['currencies'].queryset = Currency.objects.filter(
            user=self.request.user)

    currencies = forms.ModelMultipleChoiceField(queryset=None,
                                                widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Collection
        fields = ['name', 'currencies']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            }
