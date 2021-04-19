from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home/dashboard.html')


def about(request):
    print(request)
    return render(request, 'home/about.html')
