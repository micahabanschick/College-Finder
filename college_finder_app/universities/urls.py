from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.universities_page), name='universities'),
    path('/<slug:slug>', login_required(views.university_detail), name='university_detail'),
]
