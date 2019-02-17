from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def userinfo(request):
    user1 = User
    return render(request, 'accounts/profile.html', {'user1': user1})
