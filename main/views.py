from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/IndexView.html'
    model = models.Article

class DetailView(generic.DetailView):
    template_name = 'blog/DetailView.html'
    model = models.Article
    #TODO poprawic przekroczenie ilosci artykułów w bazie