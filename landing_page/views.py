from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'landing_page.html', {})

def about(request):
   return render(request, 'aboutus.html', {})

def page1(request):
    return render(request, 'page1.html', {})

def page2(request):
    return render(request, 'page2.html', {})

