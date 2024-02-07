from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Type, Activity, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ActivityForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "Invalid username or password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'base/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):  # request is HTTP object
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'base/home.html', context)

def activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    context = {'activity': activity}
    return render(request, 'base/activity.html', context)

def create_activity(request):
    context = {'sender': 'create_activity', 'act_form': ActivityForm()}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST)
        if act_form.is_valid():
            act_form.save()
            return redirect('home')

    return render(request, 'base/activity_form.html', context)

def edit_activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    form = ActivityForm(instance=activity)
    context = {'sender': 'edit_activity', 'activity': activity, 'act_form': form}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST, instance=activity)
        if act_form.is_valid():
            act_form.save()
            return redirect('activity', pk)

    return render(request, 'base/activity_form.html', context)

def delete_activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)

    context = {'type': 'activity', 'obj': activity}

    if request.method == 'POST':
        activity.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context)