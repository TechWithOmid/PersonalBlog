from django.contrib import admin
from .models import Article, Category, Author, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'publish_status']
    list_editable = ['publish_status']
    raw_id_fields = ('category',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment_summery', 'article', 'comment_date', 'active']
    list_filter = ['comment_date', 'active']
    list_search = ['name', 'email', 'body']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)
