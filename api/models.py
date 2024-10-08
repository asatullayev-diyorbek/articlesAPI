from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default.jpg'


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author/', blank=True, null=True)

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default.jpg'


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    print_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/', blank=True, null=True)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name + ' - ' + self.title[:40]

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default.jpg'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user ni ichida ism familiya va emaili bor
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = 'Sharx'
        verbose_name_plural = 'Sharxlar'

    def __str__(self):
        return self.user.get_full_name() + ' ' + self.article.title[:30]
