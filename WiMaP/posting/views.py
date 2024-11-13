from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 

# Create your views here.

def index(request):
    return render(request, 'posting/index.html')

def pilih(request):
    return render(request, 'posting/pilih.html')

def signup(request):
    return render(request, 'posting/signup.html')
