from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.http import HttpResponse
from resume.models import Resume
from vacancy.models import Vacancy
from django.shortcuts import redirect

class MenuView(View):
    def get(self, request):
        return render(request, 'hyperjob/index.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'

class ProfileView(View):
    def get(self, request):
        return render(request, 'hyperjob/home.html', {'user': request.user})