from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('category/list/', views.CategoryView.as_view(), name='category_list'),
    path('category/<int:pk>/detail/', views.CategoryView.as_view(), name='category_detail'),

    path('author/list/', views.AuthorView.as_view(), name='author_list'),
    path('author/<int:pk>/detail/', views.AuthorView.as_view(), name='author_detail'),

    path('article/list/', views.ArticleView.as_view(), name='article_list'),
    path('article/<int:pk>/detail/', views.ArticleView.as_view(), name='article_detail'),

    path('comment/list/', views.CommentView.as_view(), name='comment_list'),
    path('comment/<int:pk>/detail/', views.CommentView.as_view(), name='comment_detail'),
]