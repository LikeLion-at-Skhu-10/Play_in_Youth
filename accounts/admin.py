from django.contrib import admin
from .models import User, Quiz

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'phone', 'quiz', 'answer']
    list_display_links = ['id', 'username']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz']
    list_display_links = ['id', 'quiz']