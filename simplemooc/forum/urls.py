from django.conf.urls import url, include
from simplemooc.forum import views

app_name = 'Forum'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tag/(?P<tag>[\w_-]+)/$', views.index, name='index_tagged'),
    url(r'(?P<slug>[\w_-]+)/$', views.thread, name='thread'),
]