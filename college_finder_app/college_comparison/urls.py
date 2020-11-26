from django.urls import path
from . import views

urlpatterns = [
    path('', views.college_comparison_page, name='college_comparison')
]
