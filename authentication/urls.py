from telnetlib import LOGOUT
from django.urls import path
from authentication.views import register_user, login_user, logout_user, auth_login


app_name = 'authentication'

urlpatterns = [
    path('register',register_user, name='register'),
    path('login',login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('json', auth_login, name='json'),
]