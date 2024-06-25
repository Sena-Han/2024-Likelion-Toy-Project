from django.db import models
from signup.models import CustomUser

class GuestBook(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    write_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]