from django.urls import path
from.import views #we use period to denote import from the current directory
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.index,name='index'),
    #path('',views.displayoffer, name='specialoffer'),
    path('create/',views.create,name='create'),
    path('offer/',views.offer,name='offer'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('search/', views.SearchProduct),
    #path('',views.ProductSearchView)
    ]
