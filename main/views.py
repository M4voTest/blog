from django.shortcuts import render
from django.views import generic
from . import models
from django.shortcuts import redirect
from django.http import Http404
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/IndexView.html'
    model = models.Article

class DetailView(generic.DetailView):
    template_name = 'blog/DetailView.html'
    model = models.Article
    #TODO Przekierowanie na 404 - ErrorView
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('main:index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class AuthorView(generic.DetailView):
    template_name = 'blog/AuthorView.html'
    model = models.Author
    #TODO podlinkowac autora w detailview, ustawic przypisanie artykułów do autora, obrazki
