from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser


def anonymous_required(view_function, redirect_to=None):
    return AnonymousRequired(view_function, redirect_to)


class AnonymousRequired(object):
    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect(self.redirect_to)
        return self.view_function(request, *args, **kwargs)


@anonymous_required
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, '../templates/registration/registration.html', {"form": form})
