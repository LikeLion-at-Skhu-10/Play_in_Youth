from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            #생성한 유저모델로 로그인함.
            auth.login(request, user)
            return render(request, 'category_detail/bicycle.html', {'form':form})
        else :
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # AuthenticationForm은 아이디와 비밀번호를 검증해서 그에 맞는 유저 모델을 찾을 수 있음
        # 또 첫번째 인수가 데이터가 아니기 때문에 data=request.POST로 따로 명시해야 함.
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return render(request, 'category_detail/bicycle.html')
        else:
            return render(request, 'signin.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return render(request, 'category_detail/bicycle.html')

def find_pw(request):
    return render(request, 'find_pw.html')

def find_name(request):
    return render(request, 'find_name.html')

def reset_pw(request):
    return render(request, 'reset_pw.html')

def mypage(request):
    return render(request, 'mypage.html')