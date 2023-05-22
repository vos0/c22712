"""first_django_dz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from first import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu),
    path('profile/', views.user_profile),
    path('Голосования/', views.index, name='list-votings'),
    path('votings/<int:id>/', views.get, name='get-vote'),
    path('votings/<int:id>/submit', views.submit),
    path('Путин/', views.putin),
    path('Cyberpunk/', views.cyberpunk),
    path('Спасибо/', views.thanks),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', auth_views.LogoutView.as_view())
]
