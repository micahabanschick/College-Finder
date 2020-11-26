from django.urls import path
from . import views

urlpatterns = [
    path('', views.universities_page, name='universities')
]
