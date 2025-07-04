"""
URL configuration for todos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',views.TodoView.as_view(),name='todo'),
    path('registartion/',views.Registration.as_view()),
    path('login/',views.UserLoginView.as_view(),name="loginpage"),
    path('todolist/',views.TodolistView.as_view(),name="todolist"),
    path('tododetail/<int:PK>/',views.TodoDetailView.as_view(),name="tododet"),
    path('tododelete/<int:PK>/',views.TodoDeleteView.as_view(),name="tododel"),
    path('todoupdate/<int:PK>/',views.TodoUpdateView.as_view(),name='todoedit'),
    path('logout/',views.Logoutview.as_view()),
    
]
