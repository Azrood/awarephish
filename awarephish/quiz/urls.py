from django.urls import path

from . import views

urlpatterns = [
    path('',views.redir, name='redir'),
    path('index/', views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('conseils/', views.conseils, name='conseils'),
]