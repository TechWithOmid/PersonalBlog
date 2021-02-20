from django.contrib import admin
from .models import Comment, ReplyComment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'is_active']


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'reply_body']


admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)
