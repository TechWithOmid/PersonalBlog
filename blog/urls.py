from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('article/<slug:article_slug>/', views.ArticleDetail, name="content_page"),
    path('category/<slug:category>/', views.CategoryPage.as_view(), name="category_page"),
    path('tags/<slug:tag>/', views.TagsPage.as_view(), name="tags_page"),
    path('search/', views.SearchArticle.as_view(), name="search_article"),
]