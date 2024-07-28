from django import forms
from django.contrib.auth.models import User
from . import models
from exam import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']

from django import forms

class ExamAttemptForm(forms.Form):
    # Define form fields corresponding to the fields in the exam_attempts table
    student_id = forms.IntegerField()
    exam_id = forms.IntegerField()
    attempt_date = forms.DateField()
