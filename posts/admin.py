from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'author', 'post_cate', 'post_title', 'post_date']
    list_display_links = ['post_id', 'author']
    list_filter = ['author', 'post_cate', 'post_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_post_id', 'author', 'comment_date']
    list_display_links = ['id', 'get_post_id', 'author']
    list_filter = ['author', 'post_id__post_id', 'comment_date']

    def get_post_id(self, obj):
        return obj.post_id.post_id

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_cate']
    list_display_links = ['id', 'post_cate']