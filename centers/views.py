import email
from urllib.request import Request
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from centers.models import Area, Center
from centers.forms import CenterForm
# Create your views here.

def find_centers(request):
    return(render(request, 'findCenters.html', {}))

def find_centers_JSON(request):
    # queries the database
    centers = Center.objects.all()
    json = serializers.serialize("json",centers)
    return HttpResponse(json, content_type="application/json")

def add_center(request):
    center_form = CenterForm()
    if request.method == "POST":
        data = request.POST
        center_form = CenterForm(data)
        center = None
        if center_form.is_valid():
            center = center_form.save()
        
        areas_str = data.get("areas")
        areas = areas_str.split(" ")
        for area in areas:
            area_entry = Area.create(area)
            area_entry.save()
            area_entry.center.add(center)
        return HttpResponseRedirect(request.path_info)
    context = {'form':center_form}
    return render(request, 'addCenter.html', context) 

def get_areas_JSON(request):
    areas = Area.objects.all()
    json = serializers.serialize("json", areas)
    return HttpResponse(json, content_type="application/json")

