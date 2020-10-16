from django.shortcuts import render, HttpResponse
from dashboard.models import Hike

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def addEntry(request):
    return render(request, 'addEntry.html');

def feed(request):
    return render(request, 'feed.html' , {'hikes': Hike.objects.all()});

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})