#from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'Courses'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^(?P<pk>\d+)/$', views.details, name='details')
	url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
	url(r'^(?P<slug>[\w_-]+)/inscricao$', views.enrollment, name='enrollment'),
	
	

	]