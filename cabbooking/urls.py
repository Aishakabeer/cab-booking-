"""cabbooking URL Configuration

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
# from django.contrib import admin
# from django.urls import path,include
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('Admins/', include("admins.urls"),name='Admin'),
#     path('', views.index,name="index"),
#     path('login/', views.loginn, name="loginn"),
#     path('signup/', views.signupp, name="signupp"),
#     path('User/', include("User.urls"),name='User'),
#     path('logout/', views.logoutt, name='logoutt'),
#     path('contact/', views.contacts, name='contacts'),
#     path('vehicle/', include("Vehicle.urls"), name='vehicle'),

# ]
# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Django's built-in admin
#     path('Admins/', include("admins.urls", namespace='Admin')),  # Custom admin paths
#     path('', views.index, name="index"),
#     path('login/', views.loginn, name="loginn"),
#     path('signup/', views.signupp, name="signupp"),
#     path('User/', include("User.urls"), name='User'),
#     path('logout/', views.logoutt, name='logoutt'),
#     path('contact/', views.contacts, name='contacts'),
#     path('vehicle/', include("Vehicle.urls"), name='vehicle'),

# ]

# cabbooking/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Admins/', include("admins.urls"), name='Admin'),
    path('', views.index, name="index"),
    path('login/', views.loginn, name="loginn"),
    path('signup/', views.signupp, name="signupp"),
    path('User/', include("User.urls"), name='User'),
    path('logout/', views.logoutt, name='logoutt'),
    path('contact/', views.contacts, name='contacts'),
    path('vehicle/', include("Vehicle.urls"), name='vehicle'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),  # New admin login path
]


