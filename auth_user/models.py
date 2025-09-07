from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    study = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=(('male', 'Erkak'), ('female', 'Ayol')), blank=True, null=True)

    def __str__(self):
        return self.user.username

