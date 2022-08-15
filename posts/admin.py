from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post_cate', 'post_date']
    list_display_links = ['id', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'author', 'comment_date']
    list_display_links = ['id', 'author']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_cate']
    list_display_links = ['id', 'post_cate']