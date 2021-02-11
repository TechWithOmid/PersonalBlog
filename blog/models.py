from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


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

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
