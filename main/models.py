from django.db import models

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_author = models.CharField(max_length=200)
    article_pub_date = models.DateTimeField()

    def __str__(self):
        return self.article_title

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_description = models.TextField()
    author_photo = models.ImageField(upload_to='authors')

    def __str__(self):
        return self.author_name