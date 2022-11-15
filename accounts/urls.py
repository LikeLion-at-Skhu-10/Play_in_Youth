from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('find_pw/', views.find_pw, name='find_pw'),
    path('find_name/', views.find_name, name='find_name'),
    path('return_name/', views.return_name, name='return_name'),
    path('reset_pw/<str:id>/', views.reset_pw, name='reset_pw'),
    path('mypage/<str:id>/', views.mypage, name='mypage'), # 자기글만 보이기(id는userid)
    # path('mypage/<int:id>/<int:id>/', views.detail, name='detail'), # 모달수정,삭제(id는날짜id)
]