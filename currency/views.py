from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Currency
from custom_user import models
from .forms import CurrencyForm


def currency(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/all_currencies.html', {'currencies': currencies})


@login_required
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
    return render(request, 'currency/currency_form.html', context)


@login_required
def update_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    form = CurrencyForm(instance=currency)
    if request.method == 'POST':
        form = CurrencyForm(request.POST, request.FILES, instance=currency)
        if form.is_valid():
            currency.save()
            return redirect('/currencies')
    context = {'form': form}
    return render(request, 'currency/currency_form.html', context)


@login_required
def delete_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('/currencies')
    context = {'currency': currency}
    return render(request, 'currency/delete.html', context)
