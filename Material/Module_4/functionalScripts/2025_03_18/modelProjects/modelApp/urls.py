from django.urls import path
from .views import getData

urlpatterns = [
    path ('', getData, name='getData')
]