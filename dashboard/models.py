import datetime

from django.db import models
from django.utils import timezone



class HikeManager(models.Manager):
    def createHike(self, name, latitude, longitude, startDate, endDate, miles, elevationGain, elevationLoss, description, starred, image1, image2, image3, tag):
        hike = self.create(name=name, latitude=latitude, longitude=longitude, startDate=startDate, endDate=endDate, miles=miles,elevationGain=elevationGain,elevationLoss=elevationLoss,description=description,starred=starred,image1=image1,image2=image2,image3=image3, tag=tag)
        return hike
    
# Create your models here.
class Hike(models.Model):
    name = models.TextField(default="")

    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    startDate = models.DateField(default="0001-01-01")
    endDate = models.DateField(default="0001-01-01")

    miles = models.FloatField(default=0)
    
    elevationGain = models.FloatField(default=0)
    elevationLoss = models.FloatField(default=0)

    description = models.TextField(default="")
    starred = models.BooleanField(default=False)

    image1 = models.ImageField(default=None,upload_to="")
    image2 = models.ImageField(default=None,upload_to="")
    image3 = models.ImageField(default=None,upload_to="")

    tag=models.TextField(default="", blank=True)

    objects = HikeManager()

    def __str__(self):
        return "miles="+str(self.miles)+", elevationGain="+str(self.elevationGain)+", elevationLoss="+str(self.elevationLoss)+", description="+str(self.description)+", starred="+str(self.starred)+", tag="+str(self.tag)
    def markStarred(self, status):
        self.starred=status
        self.save()

class ImageSave(models.Model):
    image = models.ImageField(default=None,upload_to="")

class Favorite(models.Model):
    fav = models.BooleanField()