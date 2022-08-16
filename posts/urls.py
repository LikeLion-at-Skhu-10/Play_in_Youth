from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('base/', views.base, name='base'),
    path('category/', views.category, name='category'),
    path('category/<str:id>/', views.cate_detail, name='cate_detail'),
    path('category/<str:id>/cate_detail_modal/', views.cate_detail, name='cate_detail_modal'),
    path('get_write/', views.get_write, name='get_write'),
    path('write/', views.write, name='write'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('like/<str:id>/', views.likes, name="likes"),
    
    # category_detail
<<<<<<< HEAD
    path('category_detail/gardening/<str:cate>/', views.gardening, name='gardening'),
    path('category_detail/farming/<str:cate>/', views.farming, name='farming'),
    path('category_detail/yoga/<str:cate>/', views.yoga, name='yoga'),
    path('category_detail/bicycle/<str:cate>/', views.bicycle, name='bicycle'),
    path('category_detail/cooking/<str:cate>/', views.cooking, name='cooking'),
    path('category_detail/go/<str:cate>/', views.go, name='go'),
    path('category_detail/hiking/<str:cate>/', views.hiking, name='hiking'),
    path('category_detail/knitting/<str:cate>/', views.knitting, name='knitting'),
    path('category_detail/fishing/<str:cate>/', views.fishing, name='fishing'),
=======
    path('category_detail/gardening/', views.gardening, name='gardening'),
    path('category_detail/farming/', views.farming, name='farming'),
    path('category_detail/yoga/', views.yoga, name='yoga'),
    # path('category_detail/<str:cate>/', views.bicycle, name='bicycle'),
    path('category_detail/cooking/', views.cooking, name='cooking'),
    path('category_detail/go/', views.go, name='go'),
    path('category_detail/hiking/', views.hiking, name='hiking'),
    path('category_detail/knitting/', views.knitting, name='knitting'),
    path('category_detail/fishing/', views.fishing, name='fishing'),
>>>>>>> 40f5ef22dd5d75dcccfceba63422db710a71628f
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)