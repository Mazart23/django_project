from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.get_routes, name='routes')
]
