from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserForm
from .models import User
from posts.views import Post

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('mypage', user.id)
        else:
            ## 별명 중복체크
            name = request.POST['username']
            try:
                _id = User.objects.get(username=name)
            except:
                _id = None
            if _id is None:
                duplicate = "사용 가능한 별명"
            else:
                duplicate = "이미 존재하는 별명"
            ## 비밀번호 확인
            if request.POST['password1']!=request.POST['password2']:
                error_password = UserCreationForm.error_messages['password_mismatch']
            context = {
                'error_username' : duplicate,
                'form' : form
            }
            return render(request, 'signup.html', context)
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('mypage', user.id)
        else:
            return render(request, 'signin.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('category')

def find_pw(request):
    return render(request, 'find_pw.html')

def find_name(request):
    return render(request, 'find_name.html')

def reset_pw(request):
    return render(request, 'reset_pw.html')

def mypage(request, id):
    '''
    url에 user id가 아닌 username이 뜨게 하고 싶었다.
    name(별명)을 받아와서 post = Post.objects.filter(author=name)으로 하려 했는데
    name이 id가 아니라서 오류가 떴다.
    id로 만들어주려고 name.id로 수정했는데, name은 그냥 str일 뿐이었다. User 기능?을 갖고 있지 않은가보다.
    그래서 진짜 User에서 가져오기로 했다
    User.objects.get(username=name) 정보를 user에 담고 그것으로 Post를 filter하니 잘 되었다.
    '''
    if request.method == 'GET':
        user = User.objects.get(id=id)
        post = Post.objects.filter(author=user)
    return render(request, 'mypage.html', {'post':post})

def detail(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'mypage.html', {'post':post})

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