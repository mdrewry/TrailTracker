from django.shortcuts import render, HttpResponse
from dashboard.models import Hike

# Create your views here.
def index(request):
    return render(request, 'dashboard.html', {'hikes': Hike.objects.all()})