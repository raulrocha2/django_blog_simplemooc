from django.conf.urls import url, include
from simplemooc.forum import views

app_name = 'forum'

urlpatterns = [
    url(r'^', views.index, name='index')
]