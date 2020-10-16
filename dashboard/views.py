from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from dashboard.models import Hike
import json
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def addEntry(request):
    if(request.POST):
        print(request.POST.get("image"))
        Hike.objects.createHike(request.POST.get("name"),request.POST.get("latitude"),request.POST.get("longitude"),request.POST.get("startDate"),request.POST.get("endDate"),request.POST.get("miles"),request.POST.get("elevationGain"),request.POST.get("elevationLoss"),request.POST.get("description"),False,request.FILES)
        return HttpResponseRedirect('/dashboard')
    return render(request, 'addEntry.html')

def feed(request):
    hikes = Hike.objects.all();
    total_miles = 0;
    total_elevation_gain=0;
    total_elevation_loss=0;
    coords = [];
    for hike in hikes:
        total_miles += hike.miles;
        total_elevation_gain+=hike.elevationGain;
        total_elevation_loss+=hike.elevationLoss;
        coords.append({'lat': hike.latitude, 'lng': hike.longitude, 'name': hike.name});
    num_hikes = len(hikes)
    average_miles= int(total_miles/num_hikes);
    average_elevation_gain= int(total_elevation_gain/num_hikes)
    average_elevation_loss= int(total_elevation_loss/num_hikes)
    coords = json.dumps(coords);
    return render(request, 'feed.html' , {'hikes': hikes,'num_hikes':num_hikes,'total_miles': int(total_miles), 'total_elevation_gain':int(total_elevation_gain), 'total_elevation_loss':int(total_elevation_loss), 'average_miles': average_miles, 'average_elevation_gain':average_elevation_gain, 'average_elevation_loss':average_elevation_loss,'coords':coords});

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})
