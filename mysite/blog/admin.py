from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)