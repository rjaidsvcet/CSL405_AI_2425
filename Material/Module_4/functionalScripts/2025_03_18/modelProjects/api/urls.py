from django.urls import path
from .views import getData, postData

urlpatterns = [
    path ('', getData, name='getData'),
    path ('postData/', postData, name='postData')
]