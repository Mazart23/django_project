from django.forms import ModelForm
from .models import Type, Activity, Comment


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
