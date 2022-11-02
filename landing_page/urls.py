from django.urls import path
from landing_page.views import *


app_name = 'landing_page'

urlpatterns = [
    path('',index, name='base'),
    path('about/',about, name= 'aboutus'),
    path('reportform/', reportform, name='reportform'),
    path('page2/', page2, name= 'page2'),
    path('know/', article, name = 'article'),
    path('manu/', manu , name = 'manu'),
]


