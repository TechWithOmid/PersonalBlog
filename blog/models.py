from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


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


class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(verbose_name="نام لاتین")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی"

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=128, verbose_name="نام تگ")
    slug = models.SlugField(verbose_name="نام لاتین")

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

    def __str__(self):
        return self.title


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آی‌پی آدرس")

    def __str__(self):
        return self.ip_address


class Article(models.Model):
    publish_choices = (
        ('p', 'Publish'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=128, null=False, blank=False, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="آدرس")
    cover = models.ImageField(upload_to='files/images/article_cover/', verbose_name="تصویر", blank=True)
    content = RichTextField(verbose_name="محتوا")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="نویسنده")
    hits = models.ManyToManyField(IPAddress,related_name="hits", through="ArtcileHits", verbose_name="بازدیدها", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی", blank=True, null=True)
    tags = models.ManyToManyField(Tags, verbose_name="تگ",blank=True, related_name="articles")
    publish_status = models.CharField(max_length=1, choices=publish_choices, null=False,
                                      blank=False, default='d', verbose_name="وضعیت انتشار")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
    


class ArtcileHits(models.Model):
    article =  models.ForeignKey(Article, on_delete=models.CASCADE) 
    ip = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
