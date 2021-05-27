from django.urls import path, include
from . import views

urlpatterns = [
    path('currencies/', views.currency, name="currency"),
    path('currency/', include([
        path('create/', views.create_currency, name="create_currency"),
        path('update/<str:pk>/', views.update_currency, name="update_currency"),
        path('delete/<str:pk>/', views.delete_currency, name="delete_currency"),
        ])),
]
