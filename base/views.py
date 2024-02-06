from django.shortcuts import render, redirect
from .models import Type, Activity, Comment
from .forms import ActivityForm

def home(request):  # request is HTTP object
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'base/home.html', context)

def activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    context = {'activity': activity}
    return render(request, 'base/activity.html', context)

def create_activity(request):
    context = {'act_form': ActivityForm()}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST)
        if act_form.is_valid():
            act_form.save()
            return redirect('home')

    return render(request, 'base/activity_form.html', context)

def activity_edit(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    form = ActivityForm(instance=activity)
    context = {'activity': activity, 'act_form': form}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST)
        if act_form.is_valid():
            act_form.save()
            return redirect('activity', pk)

    return render(request, 'base/activity_form.html', context)