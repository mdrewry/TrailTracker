from django.contrib import admin
# Register your models here.
from .models import Hike, Favorite, ImageSave
admin.site.register(Hike)
admin.site.register(Favorite)
admin.site.register(ImageSave)