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
            'image1' : ('Enter 3 images:<br/> Image 1'),
            'image2' : ('Image 2'),
            'image3' : ('Image 3'),
            'starred' : ('Favorite Hike'),
            'startDate': ('Start Date'),
            'endDate': ('End Date'),
            'elevationGain': ('Elevation Gained'),
            'elevationLoss': ('Elevation Lost'),
            'tag': ('Tag (e.g. challenging, wildlife, rain...)')
        }