from django.contrib import admin
# Register your models here.
from .models import Hike, ToggleVar
admin.site.register(Hike)
admin.site.register(ToggleVar)
