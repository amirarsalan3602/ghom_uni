from django.contrib.auth.models import User
from django.db import models


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=2551)
    subject = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.message}'
