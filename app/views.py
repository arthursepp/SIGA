from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('login')

def login(request):
    pass

@login_required
def home(request):
    return render(request, 'home.html')
