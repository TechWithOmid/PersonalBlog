from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article


class HomePage(TemplateView):

    def get(self, request, format=None):
        articles = Article.objects.filter(publish_status='p')
        context = {
            'articles': articles
        }

        return render(request, 'home.html', context)


class ContentPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        article_id = self.kwargs.get('article_id')
        article = Article.objects.filter(publish_status='p')
        article = get_object_or_404(article, pk=article_id)

        context = {
            'article': article,
        }
        return render(request, 'content.html', context)
