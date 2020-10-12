import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Hike(models.Model):
    miles = models.FloatField()
    elevationGain = models.FloatField()
    elevationLoss = models.FloatField()
    description = models.TextField()
    starred = models.BooleanField()

    def __str__(self):
        return "miles="+str(self.miles)+", elevationGain="+str(self.elevationGain)+", elevationLoss="+str(self.elevationLoss)+", description="+str(self.description)+", starred="+str(self.starred)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text