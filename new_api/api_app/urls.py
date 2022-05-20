from django.urls import path
from .views import show_data

urlpatterns = [
    path('api/v1/show_response/', show_data, name='show_response'),
]