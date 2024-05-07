from django import forms
from .models import Exam, Project


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'examdate', 'hard']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el Titulo'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escrine la descripción'}),
            'examdate': forms.DateInput(format=('%Y-%m-%d'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'}),
            'hard': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'subject', 'examdate', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el Titulo'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escrine la descripción'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la Materia del proyecto'}),
            'examdate': forms.DateInput(format=('%Y-%m-%d'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
