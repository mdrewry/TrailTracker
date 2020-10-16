from django.shortcuts import render, HttpResponse
from dashboard.models import Hike

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def addEntry(request):
    return render(request, 'addEntry.html');

def feed(request):
    hikes = Hike.objects.all();
    total_miles = 0;
    total_elevation_gain=0;
    total_elevation_loss=0;
    for hike in hikes:
        total_miles += hike.miles;
        total_elevation_gain+=hike.elevationGain;
        total_elevation_loss+=hike.elevationLoss;
    return render(request, 'feed.html' , {'hikes': hikes, 'total_miles': total_miles, 'total_elevation_gain':total_elevation_gain, 'total_elevation_loss':total_elevation_loss});

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})