from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Category, Post, Comment
from .forms import CommentForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')


def cate_detail(request, cate_id):
    '''
    카테고리 디테일
    1) 작성자가 같아야 함
    2) 카테고리가 같아야 함
    3) 글 내용이 같아야 함
    4) 글 아이디가 같아야 함 ✔
    '''
    posts = ''
    # 해당 카테고리 글 다 가져오기
    # posts = get_object_or_404(Category, id=id) #이렇게 하면 html에서 반복을 못함
    posts = Post.objects.filter(post_cate=cate_id)
    cate_name = posts.first()

    # 각 글의 content, comment, img, author, date 가져오기(모달부분)

    context = {
        'posts':posts,
        'cate_name':cate_name
    }
    return render(request, 'category_detail.html', context)

'''
1. 해당 카테고리 글 다 가져옴
1-2. cate_detail에 글 보이기
2. 더보기를 누르면 comment view 실행
2-2. 각 글에 해당하는 댓글 다 가져옴 (Post id==Comment id)
3. 닫기를 누르면 댓글 사라짐.
'''

def cate_detail_comment(request, cate_id, post_id): # cate_id == '한글(예:자전거)', cate == '숫자(예:1)'
    cate = Category.objects.get(post_cate=cate_id) # cate id가 옴
    posts = Post.objects.filter(post_cate=cate)
    post = get_object_or_404(Post, pk=post_id)

    cmts = Comment.objects.filter(post_id=post_id)
    '''댓글'''
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post
            comment.comment_content = comment_form.cleaned_data['comment_content']
            comment.comment_date = timezone.now()
            comment.save()
            cate_id = cate.id
            return redirect('cate_detail', cate_id)
            
    else:
        comment_form = CommentForm()
        context = {
            'posts':posts,
            'post':post,
            'cmt_form':comment_form,
            'cmts':cmts,
        }
        return render(request, 'category_detail.html', context)

def category(request):
    '''카테고리 육각형 모음'''
    cates = Category.objects.all() #objects까지만 쓰면 'Manager'에 접근 못한다는 오류 뜸
    return render(request, 'category.html' ,{'cates':cates})

def write(request):
    '''if request.method == 'POST':'''
    post = Post()
    post.author = request.user
    post.post_date = timezone.now()
    post.post_title = request.POST.get('post_title')
    post.post_content = request.POST.get('post_content')
    post.post_img = request.FILES.get('post_img')
    post_cate_id = request.POST.get('post_cate') #cate의 id를 가져옴
    print("cate id 출력해보기 :: ", post_cate_id)
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
    '''method==GET'''
    # edit_post = Post.objects.get(post_id=id)
    edit_post = get_object_or_404(Post, post_id=id)
    print('img 출력 ::' , edit_post.post_img)
    # if request.method == 'POST':
    #     post = Post()
    #     user = request.user
    #     post.author = user
    #     return redirect('mypage', user.id)
    # else:
    return render(request, 'edit.html', {'edit_post':edit_post})
        
def update(request, id):
    '''method==POST && post update'''
    # update_post = get_object_or_404(Post, id=id)
    user = request.user
    update_post = Post.objects.get(post_id=id)
    update_post.post_title = request.POST['post_title']
    update_post.post_date = timezone.now()
    update_post.post_content = request.POST['post_content']
    update_post.post_img = request.FILES.get('post_img')
    update_post.save()
    return redirect('mypage', user.id)
    
def delete (request, id):
    '''post delete'''
    delete_post = Post.objects.get(post_id=id)
    delete_post.delete()
    # if request.method == 'GET':
    #     delete_post = get_object_or_404(Post, post_id=id)
    #     post = Post()
    user = request.user
    # post.author = user
    #     delete_post.delete()
    return redirect('mypage', user.id)
def delete_cmt (request, id):
    '''comment delete'''
    delete_cmt = Comment.objects.get(id=id)
    delete_cmt.delete()
    user = request.user
    return redirect('mypage', user.id)
    
# 좋아요
def likes(request, id): # 이 부분에 있는 id가 urls와 같게 작성.
    like_post = get_object_or_404(Post, post_id=id)
    if request.user in like_post.post_like.all(): 
        like_post.post_like.remove(request.user)
        like_post.like_count -= 1
        like_post.save()
    else:
        like_post.post_like.add(request.user)
        like_post.like_count += 1
        like_post.save()
    return redirect('cate_detail', like_post.post_cate.id) # id를 가져오는 방법을 모델과 관련하여 고민해봐야 함

# category_detail
def gardening(request):
    return render(request, 'category_detail/gardening.html')

def farming(request, farming):
    category = Post.objects.filter(category=farming)
    return render(request, 'category_detail/farming.html', {'category':category})

def yoga(request, yoga):
    category = Post.objects.filter(category=yoga)
    return render(request, 'category_detail/yoga.html',{'category':category})

# def bicycle(request, cate):
#     # category_posts = posts.filter(post_cate='자전거')
#     return render(request, 'category_detail/bicycle.html', cate)

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