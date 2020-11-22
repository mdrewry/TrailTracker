import datetime

from django.db import models
from django.utils import timezone



class HikeManager(models.Manager):
    def createHike(self, name, latitude, longitude, startDate, endDate, miles, elevationGain, elevationLoss, description, starred, image):
        hike = self.create(name=name, latitude=latitude, longitude=longitude, startDate=startDate, endDate=endDate, miles=miles,elevationGain=elevationGain,elevationLoss=elevationLoss,description=description,starred=starred,image=image)
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

    image = models.ImageField(default=None,upload_to="img/")

    tag=models.TextField(default="")

    objects = HikeManager()

    def __str__(self):
        return "miles="+str(self.miles)+", elevationGain="+str(self.elevationGain)+", elevationLoss="+str(self.elevationLoss)+", description="+str(self.description)+", starred="+str(self.starred)
    def markStarred(self, status):
        self.starred=status
        self.save()