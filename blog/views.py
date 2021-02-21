from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Article, Category, Tags
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment, ReplyComment
from comment.forms import CommentForm, ReplyCommentForm


class HomePage(TemplateView):

    def get(self, request, format=None):
        category = Category.objects.all()
        tags = Tags.objects.all()
        article_list = Article.objects.filter(publish_status='p').order_by('-created_date')
        paginator = Paginator(article_list, 6)

        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': category,
            'tags': tags
        }

        return render(request, 'base.html', context)


class CategoryPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()
        tags = Tags.objects.all()
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
            'tags': tags,
        }

        return render(request, 'category.html', context)


class SearchArticle(TemplateView):
    def get(self, request, format=None, **kwargs):
        cataeorys = Category.objects.all()
        tags = Tags.objects.all()

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
            'searched': searched_key,
            'tags': tags,
        }

        return render(request, 'search_result.html', context)


def ArticleDetail(request, **kwargs):
    category = Category.objects.all()
    tags = Tags.objects.all()
    article_id = kwargs.get('article_id')
    article = Article.objects.filter(publish_status='p')
    article = get_object_or_404(article, pk=article_id)
    comments = Comment.objects.filter(article=article)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        reply_comment_form = ReplyCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
        if reply_comment_form.is_valid():
            new_reply = reply_comment_form.save(commit=False)
            commentId = request.POST.get('comment_id')
            commentId = Comment.objects.get(pk=commentId)
            new_reply.comment = commentId
            new_reply.save()
    else:
        comment_form = CommentForm()
        reply_comment_form = ReplyCommentForm()

    context = {
        'article': article,
        'categorys': category,
        'comments': comments,
        'comment_form': comment_form,
        'reply_comment_form': reply_comment_form,
        'tags': tags,
    }
    return render(request, 'content.html', context)

