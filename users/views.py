from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


def home_view(request):
    return render(request, 'home.html')



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse_lazy('users:login')
    

from django.contrib.auth.views import LoginView
class MyLoginView(LoginView):
    redirect_authenticated_user = False
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('users:home')