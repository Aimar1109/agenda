import datetime
from django import forms
from .models import Exam


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
