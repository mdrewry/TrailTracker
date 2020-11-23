from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from dashboard.models import Hike, ImageSave
from dashboard.forms import HikeForm
import json
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html');

def feed(request):
    context = {}
    #Calculates hike stats and populates hike list
    hikes = Hike.objects.all();
    total_miles = 0;
    total_elevation_gain=0;
    total_elevation_loss=0;
    name_filter = request.GET.get('search','');
    coords = [];
    filtered_hikes = [];
    for hike in hikes:
        total_miles += hike.miles;
        total_elevation_gain+=hike.elevationGain;
        total_elevation_loss+=hike.elevationLoss;
        if hike.name.lower().startswith(name_filter.lower(), 0, len(name_filter)):
            coords.append({'lat': hike.latitude, 'lng': hike.longitude, 'name': hike.name});
            filtered_hikes.append(hike)

    
        
    context['hikes'] = filtered_hikes
    context['num_hikes'] = len(hikes)
    context['average_miles'] = int(total_miles/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['average_elevation_gain'] = int(total_elevation_gain/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['average_elevation_loss'] = int(total_elevation_loss/context['num_hikes']) if context['num_hikes']>0 else 0;
    context['total_miles'] = int(total_miles);
    context['total_elevation_gain'] = int(total_elevation_gain);
    context['total_elevation_loss'] = int(total_elevation_loss);
    context['coords'] = json.dumps(coords);
    context['name_filter'] = name_filter;
    return render(request, 'feed.html' , context);

def addEntry(request):
    if(request.method == "POST"):
        form = HikeForm(request.POST, request.FILES)
        starredBool = False
        if request.POST.get("starred") == 'on':
            starredBool = True
        if(form.is_valid()):
            Hike.objects.createHike(request.POST.get("name"),
            request.POST.get("latitude"),
            request.POST.get("longitude"),
            request.POST.get("startDate"),
            request.POST.get("endDate"),
            request.POST.get("miles"),
            request.POST.get("elevationGain"),
            request.POST.get("elevationLoss"),
            request.POST.get("description"),
            starredBool,
            request.FILES['image'])
            return HttpResponseRedirect('/')
    else:
        form = HikeForm()
    return render(request, 'addEntry.html', {"form" : form})

def editEntry(request, id):
    selected_hike = Hike.objects.get(pk=id)
    if(request.method == "POST"):
        form = HikeForm(request.POST, request.FILES)
        starredBool = False
        if request.POST.get("starred") == 'on':
            starredBool = True
        if(form.is_valid()):
            Hike.objects.filter(pk=id).update(
                name= request.POST.get("name"),
                description= request.POST.get("description"),
                latitude= request.POST.get("latitude"),
                longitude= request.POST.get("longitude"),
                startDate= request.POST.get("startDate"),
                endDate= request.POST.get("endDate"),
                elevationGain= request.POST.get("elevationGain"),
                elevationLoss= request.POST.get("elevationLoss"),
                starred= starredBool,
                image= request.FILES['image'],
            )

            addImage = ImageSave(image=request.FILES['image'])
            addImage.save()
            return HttpResponseRedirect('/')
    else:
        form = HikeForm(
            initial={
                'name':selected_hike.name,
                'description':selected_hike.description,
                'miles': selected_hike.miles,
                'latitude': selected_hike.latitude, 
                'longitude':selected_hike.longitude, 
                'startDate': selected_hike.startDate,
                'endDate':selected_hike.endDate,
                'elevationGain':selected_hike.elevationGain,
                'elevationLoss':selected_hike.elevationLoss,
                'starred':selected_hike.starred,
                'image':selected_hike.image})
    return render(request,'editEntry.html',{'hike':selected_hike, "form" : form})

def viewEntry(request,id):
    return render(request,'viewEntry.html',{'hike':Hike.objects.get(pk=id)})

def deleteEntry(request,id):
    hike=Hike.objects.get(pk=id)
    hike.delete()
    return HttpResponseRedirect('/')