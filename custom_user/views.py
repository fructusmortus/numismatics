from django.shortcuts import render, redirect
from .forms import RegisterForm
from home import views

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect(views.home)
    else:
        form = RegisterForm()
    return render(response, '../templates/registration/registration.html', {"form":form})
