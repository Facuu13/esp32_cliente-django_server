from django.urls import path
from .views import data_list

urlpatterns = [
    path('v1/data/', data_list),
]