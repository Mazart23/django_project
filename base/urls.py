from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('activity/<str:pk>/', views.activity, name='activity'),
    path('activity/<str:pk>/edit/', views.edit_activity, name='edit-activity'),
    path('create-activity/', views.create_activity, name='create-activity'),
    path('activity/<str:pk>/edit/delete/', views.delete_activity, name='delete-activity'),
    path('activity/<str:pk>/delete-comment/', views.delete_comment, name='delete-comment'),
    path('profile/<str:username>/', views.user_profile, name='user-profile'),
    path('profile/<str:username>/edit-user/', views.edit_user, name='edit-user')
]