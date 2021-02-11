from django.contrib import admin
from .models import Article, Category, Author


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'publish_status']
    raw_id_fields = ('category',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Author)
