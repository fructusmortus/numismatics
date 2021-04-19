from django.shortcuts import render, redirect
from .models import Currency
from .forms import CurrencyForm


def currency(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/all_currencies.html', {'currencies': currencies})


def create_currency(request):
    form = CurrencyForm()
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'currency/create_currency.html', context)


def update_currency(request):
    form = CurrencyForm()
    context = {'form': form}
    return render(request, 'currency/create_currency.html', context)
