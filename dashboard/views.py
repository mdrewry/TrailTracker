from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from dashboard.models import Hike

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
    return render(request, 'feed.html' , {'hikes': Hike.objects.all()})

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})
