from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/<str:pk>/', views.activity, name='activity'),
    path('activity/<str:pk>/edit/', views.activity_edit, name='activity-edit'),
    path('create-activity/', views.create_activity, name = 'create-activity')
]