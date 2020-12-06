from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

def __str__(self):
  return self.username
