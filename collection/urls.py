from django.urls import path, include
from .views import CreateCollection, UpdateCollection, DeleteCollection

app_name = 'collection'

urlpatterns = [
    path('collection/', include([
            path('create/', CreateCollection.as_view(), name='create_collection'),
            path('update/<str:pk>/', UpdateCollection.as_view(), name="update_collection"),
            path('delete/<str:pk>/', DeleteCollection.as_view(), name="delete_collection"),
        ])
    ),
]
