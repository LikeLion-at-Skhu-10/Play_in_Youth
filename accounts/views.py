from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def find_pw(request):
    return render(request, 'find_pw.html')

def find_name(request):
    return render(request, 'find_name.html')

def reset_pw(request):
    return render(request, 'reset_pw.html')

def mypage(request):
    return render(request, 'mypage.html')