from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Article, Category, Tags, IPAddress
from django.core.paginator import Paginator
from django.db.models import Q, F
from comment.models import Comment, ReplyComment
from comment.forms import CommentForm, ReplyCommentForm
from django.db.models import Count


# TODO 
# fix hits article 
# make article detail view class base
# make views better
# make search style better 

class HomePage(TemplateView):

    def get(self, request, format=None):
        category = Category.objects.all()
        tags = Tags.objects.all()
        article_hits = Article.objects.filter(publish_status='p').annotate(count=Count('hits'))
        article_list = Article.objects.filter(publish_status='p').order_by('-created_date')
        paginator = Paginator(article_list, 6)

        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': category,
            'tags': tags,
            'article_hits': article_hits,
        }

        return render(request, 'blog/index.html', context)


class CategoryPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        categorys = Category.objects.all()
        tags = Tags.objects.all()
        article_hits = Article.objects.filter(publish_status='p').annotate(count=Count('hits'))
        category = self.kwargs.get('category')
        article_list = Article.objects.filter(
            category__slug=category, publish_status='p'
        ).order_by('-created_date')

        paginator = Paginator(article_list, 6)
        page_number = self.request.GET.get('page')

        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': categorys,
            'tags': tags,
            'article_hits': article_hits,
        }

        return render(request, 'blog/category.html', context)


class TagsPage(TemplateView):
    def get(self, request, format=None, **kwargs):
        tag = self.kwargs.get('tag')
        tags = Tags.objects.all()
        categorys = Category.objects.all()
        article_hits = Article.objects.filter(publish_status='p').annotate(count=Count('hits'))
        article_list = Article.objects.filter(tags__slug=tag)

        paginator = Paginator(article_list, 6)
        page_number = self.request.GET.get('page')

        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'tags': tags,
            'categorys': categorys,
            'article_hits': article_hits, 
        }
        return render(request, 'blog/tags.html', context)


class SearchArticle(TemplateView):
    def get(self, request, format=None, **kwargs):
        categorys = Category.objects.all()
        tags = Tags.objects.all()
        article_hits = Article.objects.filter(publish_status='p').annotate(count=Count('hits'))

        searched_key = self.request.GET.get('q')
        article_list = Article.objects.filter(
            Q(title__icontains=searched_key) | Q(content__icontains=searched_key)
        ).order_by('-created_date')
        paginator = Paginator(article_list, 6)
        page_number = self.request.GET.get('page')

        articles = paginator.get_page(page_number)

        context = {
            'articles': articles,
            'categorys': categorys,
            'searched': searched_key,
            'tags': tags,
            'article_hits': article_hits,
        }

        return render(request, 'blog/search_result.html', context)


def ArticleDetail(request, **kwargs):
    category = Category.objects.all()
    tags = Tags.objects.all()
    article_hits = Article.objects.filter(publish_status='p').annotate(count=Count('hits'))
    article_slug = kwargs.get('article_slug')
    article_status = Article.objects.filter(publish_status='p')
    article = get_object_or_404(article_status, slug=article_slug)
    article_tags = Tags.objects.filter(articles=article)
    comments = Comment.objects.filter(article=article)
    new_comment = None


    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)


    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        reply_comment_form = ReplyCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            comment_form = CommentForm()
        if reply_comment_form.is_valid():
            new_reply = reply_comment_form.save(commit=False)
            commentId = request.POST.get('comment_id')
            commentId = Comment.objects.get(pk=commentId)
            new_reply.comment = commentId
            new_reply.save()
            reply_comment_form = ReplyCommentForm()

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
        'article_hits': article_hits,
        'article_tags': article_tags,
    }
    return render(request, 'blog/content.html', context)



