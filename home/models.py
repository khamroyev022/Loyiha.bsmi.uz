from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

# models.py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    study = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=(('Erkak', 'Erkak'), ('Ayol', 'Ayol')), blank=True, null=True)

    
    hemis_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="HEMIS ID")
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('pending', 'Pending')
        ],
        default='pending',
        verbose_name="Foydalanuvchi holati"
    )

    def __str__(self):
        return self.user.username


class File(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    @property
    def filename(self):
        """Faylning toza nomini qaytaradi (pathdan ajratib)"""
        return os.path.basename(self.file.name) if self.file else "—"
    def __str__(self):
        return f"{self.user.username} - {self.file.name}"


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username} - {self.subject}"


class yangilik(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    discription = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'yangilik'

class Tanlovlar(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    image = models.ImageField(upload_to='tanlovlar_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tanlovlar'
