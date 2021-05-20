from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Currency
from category.models import Category
from custom_user import models
from .forms import CurrencyForm
import json


def has_perm(self, perm, obj=None):
    user_perm = self.user_permissions.get(codename=perm)
    if user_perm:
        return True
    else:
        return False


def permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/')


@permission_required("currency.view_currency")
def currency(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/all_currencies.html', {'currencies': currencies})


@login_required
@permission_required("currency.add_currency")
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
@permission_required("currency.change_currency")
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
@permission_required("currency.delete_currency")
def delete_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('/currencies')
    context = {'currency': currency}
    return render(request, 'currency/delete.html', context)
