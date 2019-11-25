"""pyshop URL Configuration

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
from django.urls import path,include# add include function here,it helps in referencing our apps urls
from django.views.generic.base import TemplateView
from products import views #we use period to denote import from the current directory
from django.contrib.auth import views as auth_views

app_name='products'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    # path('',views.displayoffer, name='specialoffer'),
    path('create/', views.create, name='create'),
    path('offer/', views.offer, name='offer'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.SearchProduct),
   # path('', TemplateView.as_view(template_name='login')),
  #  path('products/',include('products.urls'))# any product url request from the user to be directed to the urls defined under product app
    #this is written only once and serves its purpose, directing products url request from the users to the defined url for the product app.
    ]
