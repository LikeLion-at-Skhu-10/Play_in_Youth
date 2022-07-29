from django.db import models
import posts.models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    user_quiz = models.CharField(max_length=50) #질문에 대한 답변 저장
    # comment_id = models.IntegerField()
    # post_id = models.IntegerField()
    
    def __str__(self):
        return self.user_id
