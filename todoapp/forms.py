from django import forms
from todoapp.models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields =["title","description","status"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "description":forms.Textarea(attrs={"class":"form-control mb-3"}),
            "status":forms.Select(attrs={"class":"form-control mb-3"})

        }




class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))
    
    class Meta:
        model = User
        fields=["username","email","password1","password2"]


        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email":forms.TextInput(attrs={"class":"form-control mb-3"})

        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))


