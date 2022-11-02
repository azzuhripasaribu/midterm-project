from django.urls import path
from landing_page.views import *


app_name = 'landing_page'


app_name = 'main'

urlpatterns = [
    path('',index, name = 'home'),
    path('reportform/', reportform, name='reportform'),
    path('page2/', page2, name= 'page2'),
    path('know/', education, name = 'article'),
    path('feedback', list_feedback, name='feedback'),
    path('json_function', json_funct, name='json_function'),
    path('fetch_feedback', fetch_post_feedback, name='fetch_feedback'),
]


