from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)
    gpa = models.DecimalField(
        decimal_places=2, max_digits=3, blank=True, null=True)
    gre_score = models.IntegerField(blank=True, null=True)
    toefl_score = models.IntegerField(blank=True, null=True)
    sop_score = models.DecimalField(
        decimal_places=1, max_digits=2, blank=True, null=True)
    lor_score = models.DecimalField(
        decimal_places=1, max_digits=2, blank=True, null=True)
    uni_score = models.IntegerField(blank=True, null=True)
    CHOICES = [(1, 'Yes'), (0, 'No')]
    research = models.IntegerField(max_length=1, choices=CHOICES, default=0)
    chance_of_admit = models.DecimalField(
        decimal_places=2, max_digits=3, blank=True, null=True, default=0.0)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
