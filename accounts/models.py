from django.db import models
from django.contrib.auth.models import AbstractUser

class Quiz(models.Model):
    quiz = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz

class User(AbstractUser):
    phone = models.CharField(max_length=100)
    # QUIZ_CHOICES=(
    #     (1,'자신이 다녔던 초등학교 이름은?'),
    #     (2,'처음 키웠던 반려동물의 이름은?'),
    #     (3,'태어난 지역은?')
    # )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='qz', null=True)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.username

# class Mypage(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     post_date = 
#     comment_date = 