from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_date', 'post_img', 'post_content']

class CommentForm(forms.ModelForm):
    '''댓글 입력하는 공간'''
    class Meta:
        model = Comment
        fields = ['comment_content']
