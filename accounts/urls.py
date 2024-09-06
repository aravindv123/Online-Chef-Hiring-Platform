from django.urls import path
from . import views  # Correctly import views from your accounts app

urlpatterns = [
    path('signup/chef/', views.chef_signup, name='chef_signup'),
    path('signup/registration/', views.registration, name='registration'),
    path('signup/user/', views.user_signup, name='user_signup'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.home, name='home'),
    path('ind/', views.indexed, name='index'),
]

