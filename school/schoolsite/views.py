from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me' :"Hello i am from views.py"}
    return render(request,'schoolsite/index.html', context=my_dict)

def signin(request):
    return render(request,'schoolsite/signin.html')

def home(request):
    return render(request,'schoolsite/index.html')

def contact(request):
    return render(request,'schoolsite/contact.html')

def about(request):
    return render(request,'schoolsite/about.html')

def gallery(request):
    return render(request,'schoolsite/gallery.html')

def admission(request):
    return render(request,'schoolsite/admission.html')

def program(request):
    return render(request,'schoolsite/program.html')

def parents(request):
    return render(request,'schoolsite/parents.html')

def news(request):
    return render(request,'schoolsite/news.html')
