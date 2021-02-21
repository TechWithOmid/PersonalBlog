from django.contrib import admin
from .models import Article, Category, Author, Tags


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'publish_status']
    list_editable = ['publish_status']
    # raw_id_fields = ('category',)
    ordering = ['-created_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)
