from django.urls import path
from . import views

urlpatterns = [
    # path ('', views.simpleFunction, name='function'),
    # path ('newPage/', views.simplePage, name='page'),
    # path ('another/', views.anotherPage, name='another')
    path ('', views.formViewer, name='forms'),
    path ('result/', views.displayInformation, name='result')
]