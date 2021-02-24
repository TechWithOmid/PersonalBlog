from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('article/<int:article_id>/', views.ArticleDetail, name="content_page"),
    path('category/<int:category_id>/', views.CategoryPage.as_view(), name="category_page"),
    path('tags/<slug:slug>', views.TagView, name="tags_page"),
    path('search/', views.SearchArticle.as_view(), name="search_article"),
]