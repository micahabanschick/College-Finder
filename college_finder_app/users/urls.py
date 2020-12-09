from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_page, name='logout'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
]
