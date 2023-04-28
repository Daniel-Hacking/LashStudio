"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from lashstore import views as store_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('', store_views.home, name='home'),
    path('services/<int:service_id>', store_views.service_detail, name='service_detail'),
    path('appointments/create', store_views.appointment_create, name='appointment_create'),
    path('appointments/list', store_views.appointment_list, name='appointment_list'),
    path('appointments/<int:appointment_id>', store_views.appointment_detail, name='appointment_detail'),
    path('appointments/cancel/<int:appointment_id>', store_views.appointment_cancel, name='appointment_cancel'),
    path('feedback/create/<int:appointment_id>', store_views.feedback_create, name='feedback_create'),
    path('admin/', admin.site.urls),
    path('users/register/', store_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
