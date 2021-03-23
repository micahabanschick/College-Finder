from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(blank=True, null=True)
    posted_on = models.DateTimeField(default=timezone.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True)
    tags = TaggableManager(blank=True, )

    def __str__(self):
        return self.title
