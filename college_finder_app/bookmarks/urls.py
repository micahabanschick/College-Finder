from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmarks_page, name='bookmarks')
]
