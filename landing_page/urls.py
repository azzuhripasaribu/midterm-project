from django.urls import path
from landing_page.views import *


app_name = 'landing_page'

urlpatterns = [
    path('',index),
    path('about',about),
    path('reportform', reportform),
    path('page2', page2),
    path('know/', article)
]


