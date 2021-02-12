from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article, Category
from django.core.paginator import Paginator
from django.db.models import Q


class HomePage(TemplateView):

    def get(self, request, format=None):
        category = Category.objects.all()
        article_list = Article.objects.filter(publish_status='p').order_by('-created_date')
        paginator = Paginator(article_list, 6)

        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': category,
        }

        return render(request, 'base.html', context)


class ContentPage(TemplateView):

    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()

        article_id = self.kwargs.get('article_id')
        article = Article.objects.filter(publish_status='p')
        article = get_object_or_404(article, pk=article_id)

        context = {
            'article': article,
            'categorys': cataeorys,
        }
        return render(request, 'content.html', context)


class CategoryPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()

        category_id = self.kwargs.get('category_id')
        articles = Article.objects.filter(category=category_id, publish_status='p')
        data = []

        for category in cataeorys:
            data.append({
                'title': category.title,
            })
        context = {
            'articles': articles,
            'categorys': cataeorys,
            'data': data,
        }

        return render(request, 'category.html', context)


class SearchArticle(TemplateView):
    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()

        searched_key = self.request.GET.get('q')
        article_list = Article.objects.filter(
            Q(title__icontains=searched_key) | Q(content__icontains=searched_key)
        )
        paginator = Paginator(article_list, 6)
        page_number = self.request.GET.get('page')

        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': cataeorys,
            'searched': searched_key
        }

        return render(request, 'search_result.html', context)
