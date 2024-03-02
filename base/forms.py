from django.forms import ModelForm
from .models import Activity, Comment

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ['host']
