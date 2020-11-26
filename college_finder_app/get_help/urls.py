from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_help_page, name='get_help')
]
