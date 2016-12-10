from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_description = models.TextField()
    author_photo = models.ImageField(upload_to='authors')


    def __str__(self):
        return self.author_name

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_author = models.ForeignKey(Author, on_delete=models.SET(get_sentinel_user))
    article_pub_date = models.DateTimeField()

    def __str__(self):
        return self.article_title
