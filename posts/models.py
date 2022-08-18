from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
 
# Create your models here.
class Category(models.Model):
    post_cate = models.CharField(max_length=300)

    def __str__(self):
        return self.post_cate

class Post(models.Model):
    # post_id = models.IntegerField() #PK는 장고에서 자동으로 생성.PK : not null&auto increment, 이름은 id로
    post_id = models.BigAutoField(help_text='post_id', primary_key=True) # 댓글 테이블에서 쓰기 위해 만듦, bigautofield = 자동증가기본키
    post_date = models.DateField(default=timezone.now) # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기
    post_title = models.CharField(max_length=100) # 불편해서 제목 추가
    post_content = models.CharField(max_length=400)
    post_img = models.ImageField(upload_to='images/', blank=True)
    
    #외래키 # 실제 테이블에서 외래키로 지정된 컬럼은 _id 접미사가 붙는다
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank = True)
    post_cate = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pst_ct', null=True)

    # 좋아요 #user model과 M:N 관계를 가지는 field
    post_like = models.ManyToManyField('accounts.User', related_name='like_users', blank=True)
    like_count = models.PositiveIntegerField(default=0) #0 또는 양수만 받는 필드

    def __str__(self):
        # return '제목:{}||작성자:{}'.format(self.post_title, self.author) #어드민 테스트
        return self.post_title

class Comment(models.Model):
    # comment_id = models.IntegerField()
    # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기 -> 날짜 선택 가능함
    comment_date = models.DateField(auto_now_add=True) # auto_now_add는 수정 불가
    comment_content = models.CharField(max_length=400)
    
    # 외래키
    #다른 테이블 참조할 때 foreign key 사용, related_name은 자신을 참조할 때 구분하기 위함
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='cmt_postid', db_column='post_id') 
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank = True)
    
    def __str__(self):
        return self.comment_content