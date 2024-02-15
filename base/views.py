from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Type, Activity, Comment
from .forms import ActivityForm


def login_view(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    context = {'page': page}
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "Invalid username")
            return render(request, 'base/login_register.html', context)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'base/login_register.html', context)

def register_view(request):
    page = 'register'
    form = UserCreationForm()
    context = {'page': page, 'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid registration data')
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
    comments = Comment.objects.filter(activity=activity)
    participants = activity.participant.all()

    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            activity=activity,
            description=request.POST.get('note')
        )
        return redirect('activity', pk)

    context = {'activity': activity, 'comments': comments, 'participants': participants}
    return render(request, 'base/activity.html', context)

@login_required(login_url='login')
def create_activity(request):
    context = {'sender': 'create_activity', 'act_form': ActivityForm()}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST)

        if act_form.is_valid():
            activity = act_form.save()
            activity.participant.add(request.user)
            return redirect('home')

    return render(request, 'base/activity_form.html', context)

@login_required(login_url='login')
def edit_activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    form = ActivityForm(instance=activity)

    if request.user != activity.host:
        return HttpResponse("Permission denied")

    context = {'sender': 'edit_activity', 'activity': activity, 'act_form': form}

    if request.method == 'POST':
        act_form = ActivityForm(request.POST, instance=activity)
        if act_form.is_valid():
            act_form.save()
            return redirect('activity', pk)

    return render(request, 'base/activity_form.html', context)

@login_required(login_url='login')
def delete_activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)

    if request.user != activity.host:
        return HttpResponse("Permission denied")

    context = {'type': 'activity', 'obj': activity}

    if request.method == 'POST':
        activity.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context)