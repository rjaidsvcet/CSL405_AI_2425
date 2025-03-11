from django.shortcuts import HttpResponse, render

# Create your views here.
def simpleFunction (request):
    return HttpResponse ('<h1>Hello World</h1>')

def simplePage (request):
    return render (request, 'index.html')

def anotherPage (request):
    return render (request, 'anotherPage.html')

def formViewer (request):
    return render (request, 'formTrial.html')

def displayInformation (request):
    firstname = request.POST ['firstname']
    return render (request, 'results.html', {'output' : firstname})
