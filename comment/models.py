from django.db import models
from blog.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article",verbose_name="مقاله مرتبط")
    name = models.CharField(max_length=80,verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(verbose_name="نظر")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ")
    is_active = models.BooleanField(default=True,verbose_name="نمایش داده شود؟")

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return self.name


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="recomment",verbose_name="پاسخ به کامنت: ")
    name = models.CharField(max_length=80,verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    reply_body = models.TextField(verbose_name="پاسخ")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ")

    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"

    def __str__(self):
        return self.name
