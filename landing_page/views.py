from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'landing_page.html', {})

def about(request):
   return render(request, 'aboutus.html', {})

def reportform(request):
    return render(request, 'reportform.html', {})

def page2(request):
    return render(request, 'page2.html', {})

def article(request):
    return render(request, 'article.html')

