""" Defines URL pattern for users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
app_name = "users"
urlpatterns = [
    #Login Page
    path('login/', LoginView.as_view(template_name='users/login.html'), 
    name='login'),
    #Logout Page
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
