from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from . import views





urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.userinfo, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
   
]