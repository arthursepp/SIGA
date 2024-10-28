from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('/accounts/login')

@login_required
def home(request, username):
    user = get_object_or_404(User, username=username)
    nome_completo = user.get_full_name
    return render(request, 'home.html', {
        'user': user,
        'nome_completo': nome_completo,
    })