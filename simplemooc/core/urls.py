#from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'core'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^contato/', views.contact, name='contact')

	]