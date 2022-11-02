from django.urls import path
from centers.views import find_centers, add_center, find_centers_JSON, get_areas_JSON


app_name = 'centers'

urlpatterns = [
        path('', find_centers, name='main'),
        path('add', add_center, name='add'),
        path('json', find_centers_JSON, name='json'),
        path('areas', get_areas_JSON, name='areajson')
]