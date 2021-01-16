from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.bookmarks_page), name='bookmarks'),
    path('/<int:id>', views.bookmark, name='toggle_bookmark'),
]
