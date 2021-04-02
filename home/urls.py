from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signupform/',views.signupform,name='signupform'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('loginform/',views.loginform,name='loginform'),
    path('logout/',views.logout,name='logout'),
    path('calculate/',views.calculate,name='calculate'),
    path('task3/',views.task3,name='task3'),
    path('task2/',views.task2,name='task2'),



]
