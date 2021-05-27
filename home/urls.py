from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<int:id>/<slug:slug>', views.category_currencies, name="category_currencies"),
    path('about/', views.about),
]
