from django.urls import path
from .views import show_data, index

urlpatterns = [
    path('', index, name='index'),
    path('api/v1/show_response/', show_data, name='show_response'),
]