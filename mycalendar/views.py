from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ExamForm
from .models import Exam

# Create your views here.


def home(request):
    return render(request, 'home.html')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect',
            })
        else:
            login(request, user)
            return redirect('home')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # resister user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],  password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'register.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


@login_required
def singout(request):
    logout(request)
    return redirect('home')


@login_required
def create_exam(request):
    if request.method == 'GET':
        return render(request, 'create_exam.html', {
                      'form': ExamForm
                      })
    else:
        try:
            form = ExamForm(request.POST)
            new_exam = form.save(commit=False)
            new_exam.user = request.user
            new_exam.save()
            return redirect('examns')
        except ValueError:
            return render(request, 'create_exam.html', {
                'form': ExamForm,
                'error': 'Por favor, introduce datos válidos'
            })


@login_required
def examns(request):
    examns = Exam.objects.filter(user=request.user)
    return render(request, 'examns.html', {
        'examns': examns
    })
