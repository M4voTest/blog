from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'article/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'author/(?P<pk>[0-9]+)/$', views.AuthorView.as_view(), name='author'),
]