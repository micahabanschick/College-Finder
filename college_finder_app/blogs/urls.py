from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.blogs_page), name='blogs'),
    path('/create', login_required(views.create_post), name='create_post'),
    path('/<slug:slug>', login_required(views.blog_detail), name='blog_detail'),
    path('/tag/<slug:slug>', login_required(views.tagged), name='tagged'),
]
