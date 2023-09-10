from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
