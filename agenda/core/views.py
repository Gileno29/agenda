from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


'''def index(request):
    return  redirect('/agenda/')'''


def login_user(request):
    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username= request.POST.get('username')
        password= request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario= request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados={'eventos': evento}
    return render(request,'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    id_envento = request.GET.get('id')
    dados={}

    if id_envento:
        dados['evento'] = Evento.objects.get(id=id_envento)
    return render(request,'evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    print(request)
    if request.POST:
        print("Entrei no metodo post")
        id= request.POST.get('id')
        titulo= request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricacao= request.POST.get('descricao')
        usuario= request.user
        print("DADOS: ", id, titulo, data_evento,descricacao,usuario)
        try:
            if id:
                 Evento.objects.filter(id=id).update(titulo=titulo, data_evento=data_evento,descricao=descricacao, usuario=usuario)
            else:
                Evento.objects.create(titulo=titulo, data_evento=data_evento,descricao=descricacao, usuario=usuario)
        except Exception as e:
            messages.error(request, "Erro ao cadastrar novo evento", e)

        return redirect('/')
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario= request.user
    evento=Evento.objects.get(id=id_evento)
    if evento.usuario==usuario:
        evento.delete()
    return redirect('/')

