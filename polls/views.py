from django.shortcuts import render, HttpResponse
from polls.models import Hike

# Create your views here.
def index(request):
    return render(request, 'index.html', {'hikes': Hike.objects.all()})