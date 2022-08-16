<<<<<<< HEAD
from django import forms
from .models import Post, Category

choices = [('bicycle', 'bicycle'), ('cooking', 'cooking'), ('farming', 'farming'), ('fishing','fishing'), ('gardening', 'gardening'), ('go', 'go'), ('hiking', 'hiking'), ('knitting', 'knitting'), ('yoga','yoga')]
# name is from model field
choice_list = []

for item in choices:
    choice_list.append(item)
=======
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comment
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ['author', 'post_date', 'post_img', 'post_content', 'hashtag']
        widget = {'category':forms.Select(choices=choice_list, attrs={'class':'form-control'})}

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
=======
        fields = ['author', 'post_date', 'post_img', 'post_content']

class CommentForm(forms.ModelForm):
    '''댓글 입력하는 공간'''
    class Meta:
        model = Comment
        fields = ['comment_content']
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f
