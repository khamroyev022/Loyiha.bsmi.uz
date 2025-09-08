from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    study = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=(('male', 'Erkak'), ('female', 'Ayol')), blank=True, null=True)

    def __str__(self):
        return self.user.username


class File(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"

