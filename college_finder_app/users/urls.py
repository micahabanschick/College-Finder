from django.urls import path
from . import views


urlpatterns = [
    path('', views.RegistrationView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
]