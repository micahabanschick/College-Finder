from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.dashboard_page, name='dashboard')
]
