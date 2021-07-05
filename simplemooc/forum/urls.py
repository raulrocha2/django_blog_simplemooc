from django.conf.urls import url, include
from simplemooc.forum import views

app_name = 'Forum'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tag/(?P<tag>[\w_-]+)/$', views.index, name='index_tagged'),
    url(r'respostas/(?P<pk>\d+)/correta/$', views.replay_correct, name='replay_correct'),
    url(r'respostas/(?P<pk>\d+)/correta/$', views.replay_incorrect, name='replay_incorrect'),
    url(r'(?P<slug>[\w_-]+)/$', views.thread, name='thread'),
]