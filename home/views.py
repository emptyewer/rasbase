from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'about/about.html')



