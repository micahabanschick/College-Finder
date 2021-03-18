from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_page, name='logout'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
    path('settings', login_required(
        views.profile_update_form), name='update_profile'),
]
