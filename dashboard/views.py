from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from dashboard.models import Hike, ToggleVar
from dashboard.forms import HikeForm
import json
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html');

def feed(request):
    try:
        ToggleVar.objects.get(pk=1)
    except:
        ToggleVar.objects.createToggleVar(False);
    context = {}
    
     #Manages edit entries toggle
    curr_toggle_state = ToggleVar.objects.get(pk=1).toggle
    if(request.method == "POST"):
        ToggleVar.objects.filter(pk=1).update(toggle= not curr_toggle_state)
        return HttpResponseRedirect('/')
    context['edit_entries'] = curr_toggle_state

    #Calculates hike stats and populates hike list
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
    context['hikes'] = hikes
    context['num_hikes'] = len(hikes)
    context['average_miles'] = int(total_miles/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['average_elevation_gain'] = int(total_elevation_gain/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['average_elevation_loss'] = int(total_elevation_loss/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['total_miles'] = int(total_miles);
    context['total_elevation_gain'] = int(total_elevation_gain);
    context['total_elevation_loss'] = int(total_elevation_loss);
    context['coords'] = json.dumps(coords);
    return render(request, 'feed.html' , context);

def addEntry(request):
    if(request.method == "POST"):
        form = HikeForm(request.POST, request.FILES)
        if(form.is_valid()):
            Hike.objects.createHike(request.POST.get("name"),request.POST.get("latitude"),request.POST.get("longitude"),request.POST.get("startDate"),request.POST.get("endDate"),request.POST.get("miles"),request.POST.get("elevationGain"),request.POST.get("elevationLoss"),request.POST.get("description"),False,request.FILES['image'])
            return HttpResponseRedirect('/')
    else:
        form = HikeForm()
    return render(request, 'addEntry.html', {"form" : form})

def editEntry(request, id):
    return render(request,'editEntry.html',{'hike':Hike.objects.get(pk=id)})

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})
