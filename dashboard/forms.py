from django import forms
from django.forms import ModelForm
from dashboard.models import Hike
class DateInput(forms.DateInput):
    input_type = 'date'

class HikeForm(ModelForm):
    class Meta:
        model = Hike
        exclude = []
        widgets = {
            'startDate': DateInput(),
            'endDate': DateInput(),
        }
        labels = {
            'starred' : ('Favorite Hike'),
            'startDate': ('Start Date'),
            'endDate': ('End Date'),
            'elevationGain': ('Elevation Gained'),
            'elevationLoss': ('Elevation Lost'),
            'tag': ('Tag (Enter tags seperated by commas)')
        }