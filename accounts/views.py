from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('bicycle')
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
            return redirect('bicycle')
        else:
            return render(request, 'signin.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('bicycle')

def find_pw(request):
    return render(request, 'find_pw.html')

def find_name(request):
    return render(request, 'find_name.html')

def reset_pw(request):
    return render(request, 'reset_pw.html')

def mypage(request):
    return render(request, 'mypage.html')