from django.shortcuts import render
from .models import Firstname

# Create your views here.

def getData (request):
    firstname = Firstname.objects.all ()
    return render (request, 'index.html', {'output' : firstname})
