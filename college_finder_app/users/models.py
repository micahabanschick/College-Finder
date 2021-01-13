from typing import Tuple
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    avatar = models.ImageField(default='avatar.svg', upload_to='profile_pics')
    country = models.TextField(null=True)
    gpa = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    gre_score = models.IntegerField(null=True)
    toefl_score = models.IntegerField(null=True)
    sop_score = models.DecimalField(decimal_places=1, max_digits=2, null=True)
    lor_score = models.DecimalField(decimal_places=1, max_digits=2, null=True)
    uni_score = models.IntegerField(null=True)
    research = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
