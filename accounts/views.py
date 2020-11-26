from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic #Create view used under generic class

# Create your views here.
class SignupView(generic.CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login') # for generic class views, only loads url when available
    template_name = 'signup.html'