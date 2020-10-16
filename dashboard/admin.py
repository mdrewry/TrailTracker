from django.contrib import admin
from dashboard.models import Hike
# Register your models here.
from .models import Hike
admin.site.register(Hike);
