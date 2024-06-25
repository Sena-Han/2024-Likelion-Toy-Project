from django.db import models
from signup.models import CustomUser

class Todolist(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title