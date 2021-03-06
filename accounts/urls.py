from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('find_pw/', views.find_pw, name='find_pw'),
    path('find_name/', views.find_name, name='find_name'),
    path('reset_pw/', views.reset_pw, name='reset_pw'),
    path('mypage/', views.mypage, name='mypage'),
]