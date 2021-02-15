from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html


class Author(models.Model):
    avatar = models.ImageField(upload_to='files/images/avatar/', blank=True)
    username = models.CharField(max_length=128, blank=False, null=False)
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    publish_choices = (
        ('p', 'Publish'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/images/article_cover/')
    content = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    publish_status = models.CharField(max_length=1, choices=publish_choices, null=False,
                                      blank=False, default='d')

    def thumbnail(self):
        return format_html(f"<img width=100 height=75 src='{self.cover.url}'>")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    @property
    def comment_summery(self):
        return truncatechars(self.body, 100)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

