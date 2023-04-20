from .models import Profile
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewProfileForm, Profile, RegisterForm
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import TemplateView, UpdateView, CreateView
# Create your views here.

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'

class NewProfile(SuccessMessageMixin, UpdateView):
    template_name = 'new_profile.html'
    form_class = NewProfileForm
    model = Profile
    success_url = '/dashboard'
    success_message = 'Profile Updated successfullly'

class UserRegistration(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login'

    