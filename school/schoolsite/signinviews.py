from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signin(request):
    signin = {'insert_me' :"Hello i am from signinviews.py"}
    return render(request,'schoolsite/signin.html',context=signin)
