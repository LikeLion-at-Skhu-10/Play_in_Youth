from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def base(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')

def write(request):
    post = Post()
    post.post_content = request.POST.get('post_content', False)
    post.post_img = request.FILES.get('post_image', False)
    post.save()
    return render(request, 'write.html')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'edit.html', {'edit_post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.post_date = timezone.localtime()
    update_post.user_id = request.POST['user_id']
    update_post.post_content = request.POST['post_content']
    update_post.post_img = request.FILES.get('post_image', False)
    update_post.save()
    return redirect('mypage', id)

def delete (request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('mypage', id)

# 좋아요

# category_detail
def gardening(request):
    return render(request, 'category_detail/gardening.html')

def farming(request):
    return render(request, 'category_detail/farming.html')

def yoga(request):
    return render(request, 'category_detail/yoga.html')

def bicycle(request):
    posts = Post.objects
    return render(request, 'category_detail/bicycle.html', {'posts':posts})

def cooking(request):
    return render(request, 'category_detail/cooking.html')

def go(request):
    return render(request, 'category_detail/go.html')

def hiking(request):
    return render(request, 'category_detail/hiking.html')

def knitting(request):
    return render(request, 'category_detail/knitting.html')

def fishing(request):
    return render(request, 'category_detail/fishing.html')