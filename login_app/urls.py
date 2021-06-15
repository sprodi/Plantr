from django.urls import path
from . import views
urlpatterns = [
   path('', views.index),
   path('create', views.create_acct),
   path('signin', views.signin),
   path('register', views.register),
   path('login', views.authenticate_user),
   path('logout', views.logout),
]