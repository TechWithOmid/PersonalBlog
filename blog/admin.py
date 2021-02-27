from django.contrib import admin
from .models import Article, Category, Author, Tags, IPAddress


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date','publish_status']
    list_editable = ['publish_status']
    ordering = ('-created_date',)
    search_fields = ('title', 'content')
    list_filter = ('publish_status', 'created_date', )


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(IPAddress)