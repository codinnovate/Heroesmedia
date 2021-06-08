from django.contrib import admin
from .models import Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','author','publish','status')
	list_filter = ('status', 'created', 'publish', 'author')
