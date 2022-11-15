from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from .forms import UserForm
from .models import User, Quiz
from posts.models import Comment
from posts.views import Post
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import CustomPasswordChangeForm, SetPasswordForm

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
            # return redirect('category')
        else:
            return render(request, 'signin.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('category')

def find_pw(request):
    if request.method == 'POST':
        phone_num = request.POST.get('find_name_phone_num')
        filted_user = User.objects.filter(phone = phone_num).first()
        correct_user = get_object_or_404(User, id=filted_user.id)
        username =  request.POST.get('find_name_nickname')
        answer = request.POST.get('find_name_answer')
        if phone_num ==  correct_user.phone:
            if correct_user.answer == answer:
                if str(correct_user) == str(username):
                    return redirect('reset_pw', correct_user.id)
                    # return render(request, 'reset_pw.html', {'correct_user':correct_user})
                else:
                    quiz = Quiz.objects.all() 
                return render(request, 'find_pw.html', {'quiz':quiz})
            else:
                quiz = Quiz.objects.all() 
                return render(request, 'find_pw.html', {'quiz':quiz})
        else:
            quiz = Quiz.objects.all() 
            render(request, 'find_pw.html', {'quiz':quiz})
    else:
        quiz = Quiz.objects.all()        
        return render(request, 'find_pw.html', {'quiz':quiz})

def find_name(request):
    if request.method == 'POST':
        phone_num = request.POST.get('find_name_phone_num')
        filted_user = User.objects.filter(phone = phone_num).first()
        correct_user = get_object_or_404(User, id=filted_user.id)
        answer = request.POST.get('find_name_answer')
        if phone_num ==  correct_user.phone:
            if correct_user.answer == answer:
                return render(request, 'return_name.html', {'correct_user':correct_user})
            else:
                quiz = Quiz.objects.all() 
                return render(request, 'find_name.html', {'quiz':quiz})
        else:
            quiz = Quiz.objects.all() 
            render(request, 'find_name.html', {'quiz':quiz})
    else:
        quiz = Quiz.objects.all()        
        return render(request, 'find_name.html', {'quiz':quiz})



def return_name(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    return render(request, 'return_name.html', user.id)

# def reset_pw(request):
#     if request.method == 'POST':
#         form = SetPasswordForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request,
#                              'Your password was successfully updated!',
#                              extra_tags='alert-success')
#             return redirect('mypage')
#         else:
#             form = PasswordChangeForm(request.user)
#         return render(request, 'reset_pw.html', {
#             'form': form,
#             # 'current_user': current_user_name,
#             # 'user_avatar': current_user_avatar
#         }) 

def reset_pw(request, id):
    """
    Complete the password reset procedure.
    """
    id = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = SetPasswordForm(user=id, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thank you! Your password has been reset. Please log in below.")
            return redirect('signin')
    else:
        form = SetPasswordForm(user=id)
        return render(request, 'reset_pw.html', {
            'title': 'Set Password',
            'form': form,
            'description': "Please enter a new password for your account.",
            'action': 'Continue',
        }) 

def mypage(request, id):
    '''
    url에 user id가 아닌 username이 뜨게 하고 싶었다.
    name(별명)을 받아와서 post = Post.objects.filter(author=name)으로 하려 했는데
    name이 id가 아니라서 오류가 떴다.
    id로 만들어주려고 name.id로 수정했는데, name은 그냥 str일 뿐이었다. User 기능?을 갖고 있지 않은가보다.
    그래서 진짜 User에서 가져오기로 했다
    User.objects.get(username=name) 정보를 user에 담고 그것으로 Post를 filter하니 잘 되었다.
    '''
    # if request.method == 'GET':
    user = request.user
    user_id = str(user.id)  
    # print(bool(user_id == id)) # True
    if (user.is_authenticated == True) and (user_id == id): # user.id 는 진짜 id이고 html에서 받아온 id는 생긴건 id지만 str이라서 str(user.id)==id로 해줘야 함.
        user = User.objects.get(id=id)
        post = Post.objects.filter(author=user)
        comment = Comment.objects.filter(author=user)
        context = {
            'post':post,
            'comment':comment
        }
        return render(request, 'mypage.html', context)
    else:
        msg = "내 정보 페이지는 로그인 후 접근 가능합니다."
        form = AuthenticationForm()
        context = {
            'msg':msg,
            'form':form
        }
        return render(request, 'signin.html', context)

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