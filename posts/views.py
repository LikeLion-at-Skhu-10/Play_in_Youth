<<<<<<< HEAD
from datetime import datetime
from operator import methodcaller
from sre_constants import CATEGORY_DIGIT
from sre_parse import CATEGORIES
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Post
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Category, Post, Comment
from .forms import CommentForm

>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')

def cate_detail(request, id):
    '''카테고리 디테일'''
    # posts = get_object_or_404(Category, id=id) #이렇게 하면 html에서 반복을 못함
    posts = Post.objects.filter(post_cate=id)
    return render(request, 'category_detail.html', {'posts':posts})
    
def cate_detail_modal(request, id):
    '''댓글'''
    post = get_object_or_404(Post, id=id)
    cmts = Comment.objects.filter(post_id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post
            comment.comment_content = comment_form.cleaned_data['cmt_content']
            comment.comment_date = timezone.now()
            comment.save()
            return redirect('cate_detail', id)
    else:
        comment_form = CommentForm()
        context = {
            'post':post,
            'cmts':cmts,
            'cmt_form':comment_form
        }
        return redirect('cate_detail', context)

def category(request):
<<<<<<< HEAD
    if request.method=='POST':
        print('post요청')
        cate = request.POST.get('bicycle')
        print(cate,'cate출력')
        return redirect('bicycle', cate)
    else:
        return render(request, 'category.html')

def write(request):
    if request.method == 'POST':
        post = Post()
        user = request.user
        post.author = user
        post.post_content = request.POST.get('post_content')
        post.post_img = request.FILES.get('post_image')
        post.post_date = timezone.now()
        post.save() 
        return redirect('mypage', user.id)
    else:
        return render(request, 'write.html')
       
def edit(request, id):
    edit_post = Post.objects.filter(id=id)
    if request.method == 'POST':
        post = Post()
        user = request.user
        post.author = user
        return redirect('mypage', user.id)
    else:
        return render(request, 'edit.html', {'edit_post':edit_post, 'post':post, 'user':user})
        
def update(request, id):
    update_post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        update_post.post_date = timezone.now()
        update_post.post_content = request.POST['post_content']
        update_post.post_img = request.FILES.get('post_image')
        update_post.save()
        return redirect('mypage', update_post.id)
    else:
        return render(request, 'edit.html')


def delete (request, id):
    if request.method == 'GET':
        delete_post = get_object_or_404(Post, id=id)
        post = Post()
        user = request.user
        post.author = user
        delete_post.delete()
    return redirect('mypage', user.id)
=======
    '''카테고리 육각형 모음'''
    cates = Category.objects.all() #objects까지만 쓰면 'Manager'에 접근 못한다는 오류 뜸
    return render(request, 'category.html' ,{'cates':cates})

def write(request):
    '''if request.method == 'POST':'''
    post = Post()
    post.author = request.user
    post.post_date = timezone.now()
    post.post_content = request.POST['post_content']
    post.post_img = request.FILES.get('post_img')
    post_cate_id = request.POST.get('post_cate') #cate의 id를 가져옴
    post.post_cate = Category.objects.get(id=post_cate_id) #cate의 id에 해당하는 Category모델에서 object를 불러와봤는데 디비에저장된이름(한글) 그대로 옴

    # post.post_cate = request.POST.get('post_cate')
    post.save() 
    return redirect('cate_detail', post_cate_id)

    '''이 밑에 방법으로 해봤는데 url이 /category/id/가 아니라 write로 됐음'''
    # posts = Post.objects.filter(post_cate=post_cate_id)
    # return render(request, 'category_detail.html', {'posts':posts})
    
def get_write(request):
    '''if request.method=='GET:'''
    post_cate = Category.objects.all()
    return render(request, 'write.html', {'post_cate':post_cate})

def edit(request, id):
    edit_post = Post.objects.filter(id=id)
    if request.method == "POST":
        edit_post.post_date = timezone.localtime()
        edit_post.post_content = request.POST['post_content']
        edit_post.post_img = request.FILES.get('post_image', False)
        edit_post.save()
        return redirect('mypage', id)
    else:
        return render(request, 'edit.html')

def update(request, id):
    update_post = Post.objects.filter(id=id)
    if request.method == "POST":
        update_post.post_date = timezone.localtime()
        update_post.post_content = request.POST['post_content']
        update_post.post_img = request.FILES.get('post_image', False)
        update_post.save()
        return render(request, 'mypage.html')
    else:
        return render(request, 'edit.html')

def delete (request, id):
    delete_post = Post.objects.filter(id = id)
    delete_post.delete()
    return render(request, 'mypage.html')
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f

# 좋아요
def likes(request, id):
    like_post = get_object_or_404(Post, id=id)
    if request.user in like_post.like.all():
        like_post.like.remove(request.user)
        like_post.like_count -= 1
        like_post.save()
    else:
        like_post.like.add(request.user)
        like_post.like_count += 1
        like_post.save()
<<<<<<< HEAD
    return redirect('/posts/category_detail/' + str(id))
=======
    return redirect('/posts/category_detail/category/' + str(id))
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f

# category_detail
def gardening(request, gardening):
    category = Post.objects.filter(category=gardening)
    return render(request, 'category_detail/gardening.html', {'category':category})

def farming(request, farming):
    category = Post.objects.filter(category=farming)
    return render(request, 'category_detail/farming.html', {'category':category})

def yoga(request, yoga):
    category = Post.objects.filter(category=yoga)
    return render(request, 'category_detail/yoga.html',{'category':category})

<<<<<<< HEAD
def bicycle(request, bicycle):
    category = Post.objects.filter(category=bicycle)
    return render(request, 'category_detail/bicycle.html', {'category':category})
=======
# def bicycle(request, cate):
#     # category_posts = posts.filter(post_cate='자전거')
#     return render(request, 'category_detail/bicycle.html', cate)
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f

def cooking(request, cooking):
    category = Post.objects.filter(category=cooking)
    return render(request, 'category_detail/cooking.html', {'category':category})

def go(request, go):
    category = Post.objects.filter(category=go)
    return render(request, 'category_detail/go.html', {'category':category})

def hiking(request, hiking):
    category = Post.objects.filter(category=hiking)
    return render(request, 'category_detail/hiking.html', {'category':category})

def knitting(request, knitting):
    category = Post.objects.filter(category=knitting)
    return render(request, 'category_detail/knitting.html', {'category':category})

def fishing(request, fishing):
    category = Post.objects.filter(category=fishing)
    return render(request, 'category_detail/fishing.html', {'category':category})