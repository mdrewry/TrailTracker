from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from dashboard.models import Hike
from .forms import HikeForm
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def addEntry(request):
    if(request.method == "POST"):
        form = HikeForm(request.POST, request.FILES)
        if(form.is_valid()):
            Hike.objects.createHike(request.POST.get("name"),request.POST.get("latitude"),request.POST.get("longitude"),request.POST.get("startDate"),request.POST.get("endDate"),request.POST.get("miles"),request.POST.get("elevationGain"),request.POST.get("elevationLoss"),request.POST.get("description"),False,request.FILES['image'])
            return HttpResponseRedirect('')
    else:
        form = HikeForm()
    return render(request, 'addEntry.html', {"form" : form})

def feed(request):
    return render(request, 'feed.html' , {'hikes': Hike.objects.all()})

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})
