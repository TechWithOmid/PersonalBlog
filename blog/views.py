from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article, Category




class HomePage(TemplateView):

    def get(self, request, format=None):
        cataeorys = Category.objects.all()
        articles = Article.objects.filter(publish_status='p').order_by('-created_date')
        context = {
            'articles': articles,
            'categorys': cataeorys,
        }

        return render(request, 'home.html', context)


class ContentPage(TemplateView):

    def get(self, request, format=None, **kwargs):
        catagorys = Category.objects.all()
        article_id = self.kwargs.get('article_id')
        article = Article.objects.filter(publish_status='p')
        article = get_object_or_404(article, pk=article_id)

        context = {
            'article': article,
            'categorys': catagorys,
        }
        return render(request, 'content.html', context)


class CategoryPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        category_id = self.kwargs.get('category_id')
        articles = Article.objects.filter(category=category_id)
        catagorys = Category.objects.all()
        context = {
            'articles': articles,
            'categorys': catagorys
        }

        return render(request, 'category.html', context)
