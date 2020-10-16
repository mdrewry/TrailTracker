import datetime

from django.db import models
from django.utils import timezone



class HikeManager(models.Manager):
    def createHike(self, name, latitude, longitude, startDate, endDate, miles, elevationGain, elevationLoss, description, starred):
        hike = self.create(name=name, latitude=latitude, longitude=longitude, startDate=startDate, endDate=endDate, miles=miles,elevationGain=elevationGain,elevationLoss=elevationLoss,description=description,starred=starred)
        return hike
    
# Create your models here.
class Hike(models.Model):
    name = models.TextField()

    latitude = models.FloatField()
    longitude = models.FloatField()

    startDate = models.DateField()
    endDate = models.DateField()

    miles = models.FloatField()
    
    elevationGain = models.FloatField()
    elevationLoss = models.FloatField()

    description = models.TextField()
    starred = models.BooleanField()
    objects = HikeManager()

    def __str__(self):
        return "miles="+str(self.miles)+", elevationGain="+str(self.elevationGain)+", elevationLoss="+str(self.elevationLoss)+", description="+str(self.description)+", starred="+str(self.starred)
    def markStarred(self, status):
        self.starred=status
        self.save()