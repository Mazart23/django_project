from django.forms import ModelForm
from .models import Activity, Comment
from django.contrib.auth.models import User

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ['host']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
