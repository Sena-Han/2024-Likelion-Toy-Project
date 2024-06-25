from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.CharField(max_length=15, unique=True)
    list_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    major = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.id
        super().save(*args, **kwargs)

class MyPage(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    introduction = models.TextField(max_length=500, blank=True, null=True)
    mbti = models.CharField(max_length=4, blank=True, null=True)
    hobby = models.CharField(max_length=200, blank=True, null=True)
    favorite_foods = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username