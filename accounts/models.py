from django.db import models
from django.contrib.auth.models import AbstractUser

class Quiz(models.Model):
    quiz = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz

class User(AbstractUser):
    phone = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    # 외래키
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='qz', null=True)

    def __str__(self):
        return self.username