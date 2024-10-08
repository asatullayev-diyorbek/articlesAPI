from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Comment, Category, Author, Article


class CategoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                return Response(
                    {
                        'id': category.id,
                        'title': category.title,
                        'image': category.get_image(),
                    }
                )
            except:
                return Response({'message': "Kategoriya topilmadi"})
        category_list = []
        categories = Category.objects.all()
        for category in categories:
            category_list.append(
                {
                    'id': category.id,
                    'title': category.title,
                    'image': category.get_image(),
                }
            )
        return Response(category_list)


class AuthorView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                author = Author.objects.get(pk=pk)
                return Response(
                    {
                        'id': author.id,
                        'first_name': author.first_name,
                        'last_name': author.last_name,
                        'image': author.get_image(),
                    }
                )
            except:
                return Response({'message': "Muallif topilmadi"})
        author_list = []
        authors = Author.objects.all()
        for author in authors:
            author_list.append(
                {
                    'id': author.id,
                    'first_name': author.first_name,
                    'last_name': author.last_name,
                    'image': author.get_image(),
                }
            )
        return Response(author_list)


class ArticleView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                article = Article.objects.get(pk=pk)
                return Response(
                    {
                        'id': article.id,
                        'title': article.title,
                        'category': article.category.title,
                        'print_date': article.print_date,
                        'content': article.content,
                        'author': {
                            'id': article.author.id,
                            'first_name': article.author.first_name,
                            'last_name': article.author.last_name,
                            'image': article.author.get_image(),
                        }
                    }
                )
            except:
                return Response({'message': "Maqola topilmadi"})

        article_list = []
        articles = Article.objects.all()
        for article in articles:
            article_list.append(
                {
                    'id': article.id,
                    'title': article.title,
                    'category': article.category.title,
                    'print_date': article.print_date,
                    'content': article.content,
                    'author': {
                        'id': article.author.id,
                        'first_name': article.author.first_name,
                        'last_name': article.author.last_name,
                        'image': article.author.get_image(),
                    }
                }
            )
        return Response(article_list)


class CommentView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                return Response(
                    {
                        'article': {
                            'id': comment.article.id,
                            'title': comment.article.title,
                            'image': comment.article.get_image(),
                        },
                        'user': {
                            'id': comment.user.id,
                            'username': comment.user.username,
                            'first_name': comment.user.first_name,
                            'last_name': comment.user.last_name,
                            'email': comment.user.email
                        },
                        'content': comment.content,
                        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                    }
                )
            except:
                return Response({'message': "Sharx topilmadi"})

        comment_list = []
        comments = Comment.objects.all()
        for comment in comments:
            comment_list.append(
                {
                    'article': {
                        'id': comment.article.id,
                        'title': comment.article.title,
                        'image': comment.article.get_image(),
                    },
                    'user': {
                        'id': comment.user.id,
                        'username': comment.user.username,
                        'first_name': comment.user.first_name,
                        'last_name': comment.user.last_name,
                        'email': comment.user.email
                    },
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                }
            )
        return Response(comment_list)
