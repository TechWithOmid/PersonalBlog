from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, Author, Category


class HomePage(TemplateView):

    def get(self, request, format=None):
        articles = Article.objects.filter(publish_status='p')
        context = {
            'articles': articles
        }

        return render(request, 'home.html', context)
