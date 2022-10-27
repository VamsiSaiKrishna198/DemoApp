"""DemoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

from chatapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/',views.homepage1,name='homepage1'),
    path('home3/',views.homepage1,name='homepage1'),
    path('home/', views.homepage, name='homepage'),
    path('',views.homepage,name='homepage'),
    path('loginpage.html/',views.loginpage,name='loginpage'),
    path('newuser.html/',views.newuser,name='username'),
    path('home2/',views.homepage1,name='homepage1'),
    path('loginpage.html/home1.html',views.homepage1,name='homepage1'),
    path('loginpage.html/home.html',views.homepage,name='homepage'),
    path('loginpage.html/home.html/homepage2.html',views.homepage2,name='homepage2'),
    path('reservation.html/',views.reservation,name='reservation'),
    path('mumbai/',views.mumbai),
    path('reservation.html/payment/',views.payment),
    path('newuser.html/loginpage.html/',views.loginpage),
]
