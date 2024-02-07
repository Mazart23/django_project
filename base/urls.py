from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('activity/<str:pk>/', views.activity, name='activity'),
    path('activity/<str:pk>/edit/', views.edit_activity, name='edit-activity'),
    path('create-activity/', views.create_activity, name='create-activity'),
    path('activity/<str:pk>/edit/delete', views.delete_activity, name='delete-activity')
]