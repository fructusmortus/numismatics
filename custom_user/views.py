from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, '../templates/registration/registration.html', {"form": form})


def custom_user(request, pk):
    custom_user = CustomUser.objects.get(id=pk)

    currency = custom_user.currency_set.all()

    context = {'custom_user': custom_user}
    return render(request, 'custom_user_info/custom_user.html', context)
