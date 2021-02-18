from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html


class Author(models.Model):
    avatar = models.ImageField(upload_to='files/images/avatar/', blank=True, verbose_name="آواتار")
    username = models.CharField(max_length=128, blank=False, null=False, verbose_name="نام‌کاربری")
    name = models.CharField(max_length=128, blank=False, verbose_name="نام")
    description = models.TextField(blank=False, null=False, verbose_name="توضیحات")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسنده ها"

    def __str__(self):
        return self.name


class Article(models.Model):
    publish_choices = (
        ('p', 'Publish'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=128, null=False, blank=False, verbose_name="عنوان")
    cover = models.ImageField(upload_to='files/images/article_cover/', verbose_name="تصویر")
    content = RichTextField(verbose_name="محتوا")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="نویسنده")
    category = models.ManyToManyField('Category', verbose_name="دسته‌بندی")
    publish_status = models.CharField(max_length=1, choices=publish_choices, null=False,
                                      blank=False, default='d', verbose_name="وضعیت انتشار")


    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name="نام دسته‌بندی")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی"

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="مقاله‌ی مرتبط")
    name = models.CharField(max_length=80, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(verbose_name="کامنت")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    active = models.BooleanField(default=False, verbose_name="نمایش داده شود؟")

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    @property
    def comment_summery(self):
        verbose_name="خلاصه"
        return truncatechars(self.body, 100)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



