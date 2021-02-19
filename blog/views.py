from django.shortcuts import render, get_object_or_404, redirect
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


def ArticleDetail(request, **kwargs):
    category = Category.objects.all()
    article_id = kwargs.get('article_id')
    article = Article.objects.filter(publish_status='p')
    article = get_object_or_404(article, pk=article_id)

    context = {
        'article': article,
        'categorys': category,
    }
    return render(request, 'content.html', context)


# def ArticleComment(request, **kwargs):
#     article_id = kwargs.get('article_id')
#     category = Category.objects.all()
#     new_comment = None
#
#     if request == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article_id
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'categorys': category,
#         'new_comment': new_comment,
#         'comment_form': comment_form,
#     }
#

# def ArticleDetail(request, **kwargs):
#     category = Category.objects.all()
#     article_id = kwargs.get('article_id')
#     a = Article.objects.filter(publish_status='p')
#     article = get_object_or_404(a, pk=article_id)
#
#     comments = Comment.objects.filter(active=True, article=article_id)
#     new_comment = None
#
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'article': article,
#         'categorys': category,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': comment_form,
#     }
#     return render(request, 'content.html', context)
