from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import Category


@login_required
def home(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'home/dashboard.html', context)


def about(request):
    print(request)
    return render(request, 'home/about.html')
