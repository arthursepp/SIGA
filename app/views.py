from django.shortcuts import render, redirect

def index(request):
    return redirect('accounts/login')

def aluno(request):
    return render(request, 'aluno.html')