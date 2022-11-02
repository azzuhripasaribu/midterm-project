from django.urls import path
from landing_page.views import *


app_name = 'landing_page'


app_name = 'main'

urlpatterns = [
    path('',index, name = 'home'),
    path('feedback', list_feedback, name='feedback'),
    path('json_function', json_funct, name='json_function'),
    path('fetch_feedback', fetch_post_feedback, name='fetch_feedback'),
]


