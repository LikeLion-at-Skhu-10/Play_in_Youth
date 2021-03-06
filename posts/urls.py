from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('base/', views.base, name='base'),
    path('category/', views.category, name='category'),
    path('write/', views.write, name='write'),
    path('edit/', views.edit, name='edit'),
    # category_detail
    path('category_detail/gardening/', views.gardening, name='gardening'),
    path('category_detail/farming/', views.farming, name='farming'),
    path('category_detail/yoga/', views.yoga, name='yoga'),
    path('category_detail/bicycle/', views.bicycle, name='bicycle'),
    path('category_detail/cooking/', views.cooking, name='cooking'),
    path('category_detail/go/', views.go, name='go'),
    path('category_detail/hiking/', views.hiking, name='hiking'),
    path('category_detail/knitting/', views.knitting, name='knitting'),
    path('category_detail/fishing/', views.fishing, name='fishing'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)