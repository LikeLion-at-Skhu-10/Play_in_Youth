from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('base/', views.base, name='base'),
    path('category/', views.category, name='category'),
    path('category/<str:cate_id>/', views.cate_detail, name='cate_detail'),
    path('category/<str:cate_id>/<str:post_id>/', views.cate_detail_comment, name='cate_detail_comment'),
    path('get_write/', views.get_write, name='get_write'),
    path('write/', views.write, name='write'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('like/<str:id>/', views.likes, name="likes"),
    
    # category_detail
    path('category_detail/gardening/', views.gardening, name='gardening'),
    path('category_detail/farming/', views.farming, name='farming'),
    path('category_detail/yoga/', views.yoga, name='yoga'),
    # path('category_detail/<str:cate>/', views.bicycle, name='bicycle'),
    path('category_detail/cooking/', views.cooking, name='cooking'),
    path('category_detail/go/', views.go, name='go'),
    path('category_detail/hiking/', views.hiking, name='hiking'),
    path('category_detail/knitting/', views.knitting, name='knitting'),
    path('category_detail/fishing/', views.fishing, name='fishing'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)