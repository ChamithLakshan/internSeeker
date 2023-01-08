from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signup_intern', views.signup_intern, name='signup_intern'),
    path('signup_company', views.signup_company, name='signup_company'),
    path('login_intern', views.login_intern, name='login_intern'),
    path('login_company', views.login_company, name='login_company'),
]