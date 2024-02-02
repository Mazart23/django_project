from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/<str:pk>/', views.activity, name='activity')
]