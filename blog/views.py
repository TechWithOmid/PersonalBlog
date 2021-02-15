from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm


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


class CategoryPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()

        category_id = self.kwargs.get('category_id')
        articles = Article.objects.filter(
            category=category_id, publish_status='p'
        ).order_by('-created_date')

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
        ).order_by('-created_date')
        paginator = Paginator(article_list, 6)
        page_number = self.request.GET.get('page')

        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': cataeorys,
            'searched': searched_key
        }

        return render(request, 'search_result.html', context)


class ContentPage(TemplateView):
    cataeorys = Category.objects.all()
    comment_form = CommentForm()

    context = {
        'categorys': cataeorys,
        'comment_form': comment_form,

    }

    def post(self, request, format=None, **kwargs):

        if self.comment_form.is_valid():
            new_comment = self.comment_form.save(commit=False)
            new_comment.article = request.POST.get('article')
            new_comment.save()

            self.context['new_comment'] = new_comment

    def get(self, request, format=None, **kwargs):
        comments = Comment.objects.filter(active=True).order_by('-comment_date')
        article_id = self.kwargs.get('article_id')
        article = Article.objects.filter(publish_status='p')
        article = get_object_or_404(article, pk=article_id)
        self.context['article'] = article
        self.context['comments'] = comments
        print(self.context.keys())
        return render(request, 'content.html', self.context)


def ArticleDetail(request, **kwargs):
    category = Category.objects.all()
    article_id = kwargs.get('article_id')
    article = Article.objects.filter(publish_status='p')
    article = get_object_or_404(article, pk=article_id)

    comments = Comment.objects.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            email = comment_form.cleaned_data['email']
            body = comment_form.cleaned_data['body']

            new_comment = name.save(commit=False)
            new_comment.email = email
            new_comment.body = body
            new_comment.article = article_id
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'article': article,
        'categorys': category,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'content.html', context)
