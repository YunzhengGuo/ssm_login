from django import forms
from .models import Student, Tlogin


class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label="姓名",
        max_length=2000,
        help_text='最大长度为2000'
       
    )
    id = forms.CharField(
        label="学号",
        max_length=2000,
        help_text='最大长度为2000',
       
    )
    
    
    class Meta:
        model = Student
        fields = ['id', 'name']


class TloginForm(forms.ModelForm):
    name = forms.CharField(
        label="姓名",
        max_length=2000,
        help_text='最大长度为2000',
      
    )
    id = forms.CharField(
        label="学号",
        max_length=2000,
        help_text='最大长度为2000',
        
    )
    class Meta:
        model = Tlogin
        fields = ['id', 'name']