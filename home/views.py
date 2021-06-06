from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import Category
from currency.models import Currency
from collection.models import Collection


@login_required
def home(request):
    category = Category.objects.all()
    collections = Collection.objects.all()
    context = {'category': category, 'collections': collections}
    return render(request, 'home/dashboard.html', context)


@login_required
def category_currencies(request, id, slug):
    currencies = Currency.objects.filter(category_id=id)
    context = {'currencies': currencies}
    return render(request, 'currency/all_currencies.html', context)


def about(request):
    print(request)
    return render(request, 'home/about.html')
