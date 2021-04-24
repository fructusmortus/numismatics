from django.shortcuts import render, redirect
from .models import Currency
from custom_user import models
from .forms import CurrencyForm


def currency(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/all_currencies.html', {'currencies': currencies})


def create_currency(request):
    form = CurrencyForm()
    if request.method == 'POST':
        form = CurrencyForm(request.POST, request.FILES)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.user = request.user
            currency.save()
            return redirect('/currencies')
    context = {'form': form}
    return render(request, 'currency/create_currency.html', context)


def update_currency(request):
    form = CurrencyForm()
    context = {'form': form}
    return render(request, 'currency/create_currency.html', context)
