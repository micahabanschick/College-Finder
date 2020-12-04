from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('', views.register_page, name='register'),
]