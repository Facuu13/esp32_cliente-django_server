from django.urls import path
from .views import data_mock

urlpatterns = [
    path('v1/data/', data_mock),
]