from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

    if senha != confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais tente novamente.')
        return redirect('/usuarios/cadastro')
    
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 6 caracteres.')
        return redirect('/usuarios/cadastro')
    
    users = User.objects.filter(username=username)
    if users.exists():
        messages.add_message(request, constants.ERROR, 'Usuário já cadastrado, utilize outro nome.')
        redirect('/usuarios/cadastro')

    user = User.objects.create_user(
        username=username,
        password=senha
    )

    return redirect('/usuarios/logar')


def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')