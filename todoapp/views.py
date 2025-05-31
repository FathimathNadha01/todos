from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp.forms import TodoForm,RegistrationForm,LoginForm
from todoapp.models import User,Todo
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



    
class Registration(View):
    def get(self,request,*args,**kwargs):
        form_instance=RegistrationForm()
        return render(request,"registration.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=RegistrationForm(request.POST)
        
        if form_instance.is_valid():
            # data=form_instance.changed_data #this done in normal form
            # qs=User.objects.create(**data)

            form_instance.save() #this done in model form ,cleaned data and query automatically done in model form

        return render(request,"registration.html")
    
class UserLoginView(View):
    def get(self,request,*args,**kwargs):
        form_instance=LoginForm()
        return render(request,'login.html',{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #remove errors
            uname=data.get("username") #to get value in dictionary
            pwd=data.get("password")
        user_obj=authenticate(request,username=uname,password=pwd) #to check its correct username and password
        if user_obj:
            login(request,user_obj) # if it is correct then login work
            return redirect('todo')
            
            
        messages.success(request,"login fail")
        return render(request,'login.html',{"form":form_instance})
    
class TodoView(View):
    def get(self,request,*args,**kwargs):
        form_instance=TodoForm()
        return render(request,'todo.html',{"form":form_instance})
    def post(self,request,*args,**kwargs):

        form_instance=TodoForm(request.POST)
        if form_instance.is_valid():
            form_instance.instance.user=request.user #todoform's model is instance here
            form_instance.save()

        return redirect("todolist")
    
class TodolistView(View):
    def get(self,request,*args,**kwargs):
        qs=Todo.objects.filter(user=request.user)#only users list can view

        return render(request,'todolist.html',{"data":qs})
    
class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("PK")
        todo_obj=Todo.objects.get(id=id,user=request.user)
        return render(request,"tododetail.html",{"data":todo_obj})
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("PK")
        Todo.objects.get(id=id,user=request.user).delete()
        return redirect("todolist")
    
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("PK")
        todo_obj=Todo.objects.get(id=id,user=request.user)
        form_instance=TodoForm(instance=todo_obj)
        return render(request,"todoedit.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("PK")
        todo_obj=Todo.objects.get(id=id,user=request.user)
        form_instance=TodoForm(request.POST,instance=todo_obj)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("todolist")
        return render(request,"todoedit.html",{"form":form_instance})

class Logoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("loginpage")


    

    

    
    


            

# Create your views here.
