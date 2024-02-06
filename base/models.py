from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    update_dt = models.DateTimeField(auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now, blank=True)

    def default_end_time():
        return timezone.now() + timedelta(hours=1)

    end_time = models.DateTimeField(default=default_end_time, blank=True)
    is_shared = models.BooleanField(default=False)
    update_dt = models.DateTimeField(auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    update_dt = models.DateTimeField(auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)
