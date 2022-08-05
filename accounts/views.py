from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
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
            # 회원가입 중복체크.. 아직 미완성
            context = {
                'msg' : "회원가입 실패. 이유 : 1)별명 중복 2)비번 형식 틀림 3)빈 입력 존재",
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