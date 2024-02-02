from django.shortcuts import render
from .models import Type, Activity, Comment


def home(request):  # request is HTTP object
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'base/home.html', context)

def activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    context = {'activity': activity}
    return render(request, 'base/activity.html', context)
