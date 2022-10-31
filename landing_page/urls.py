from django.urls import path
from landing_page.views import *


app_name = 'landing_page'

urlpatterns = [
    path('',index),
    path('about',about),
    path('page1', page1),
    path('page2', page2),
    path('know/', education)
]


