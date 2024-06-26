from datetime import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ExamForm, ProjectForm
from .models import Exam, Project

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
        return render(request, 'exam/create_exam.html', {
                      'form': ExamForm
                      })
    else:
        try:
            form = ExamForm(request.POST)
            new_exam = form.save(commit=False)
            new_exam.user = request.user
            new_exam.save()
            return redirect('exams')
        except ValueError:
            return render(request, 'exam/create_exam.html', {
                'form': ExamForm,
                'error': 'Por favor, introduce datos válidos'
            })


@login_required
def exams(request):
    exams = Exam.objects.filter(user=request.user)
    return render(request, 'exam/exams.html', {
        'exams': exams
    })


@login_required
def exam_detail(request, exam_id):
    if request.method == 'GET':
        exam = get_object_or_404(Exam, pk=exam_id, user=request.user)
        form = ExamForm(instance=exam)
        return render(request, 'exam/exam_detail.html', {
            'exam': exam,
            'form': form
        })
    else:
        try:
            exam = get_object_or_404(Exam, pk=exam_id, user=request.user)
            form = ExamForm(request.POST, instance=exam)
            form.save()
            return redirect('exams')
        except ValueError:
            return render(request, 'exam/exam_detail.html', {
                'exam': exam,
                'form': form,
                'error': 'Error actualizando datos.'
            })


@login_required
def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id, user=request.user)
    if request.method == 'POST':
        exam.delete()
        return redirect('exams')


@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, 'project_/create_project.html', {
            'form': ProjectForm
        })
    else:
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'project_/create_project.html', {
                'form': ProjectForm,
                'error': 'Por favor, introduce datos válidos'
            })


@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project_/projects.html', {
        'projects': projects
    })


@login_required
def project_detail(request, project_id):
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id, user=request.user)
        form = ProjectForm(instance=project)
        return render(request, 'project_/project_detail.html', {
            'project': project,
            'form': form
        })
    else:
        try:
            project = get_object_or_404(
                Project, pk=project_id, user=request.user)
            form = ProjectForm(request.POST, instance=project)
            form.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'project_/project_detail.html', {
                'project': project,
                'form': form,
                'error': 'Error actualizando datos.'
            })


@login_required
def complete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.datecomplete = timezone.now()
        project.save()
        return redirect('projects')


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
