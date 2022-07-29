from django.db import models
from django.conf import settings
import accounts.models

# Create your models here.
class Post(models.Model):
    # post_id = models.IntegerField()
    post_date = models.DateField(auto_now_add=True) # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기
    post_content = models.CharField(max_length=400)
    post_img = models.ImageField(upload_to='images/', blank=True)
    # post_like = # 좋아요
    
    def __str__(self):
        return self.post_content

class Comment(models.Model):
    # comment_id = models.IntegerField()
    comment_date = models.DateField(auto_now_add=True) # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기
    comment_content = models.CharField(max_length=400)

    def __str__(self):
        return self.comment_content