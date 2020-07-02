#from django.contrib.auth import login
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts import views
from django.conf import settings
app_name = 'accounts'

urlpatterns = [
	#url(r'^entrar/', include('django.contrib.auth.urls'),
	 #{'template_name': 'accounts/login.html'}, name='login'),
	url(r'entrar/', LoginView.as_view(), 
	{'template_name': 'registration/login.html'}, name='login'),
	url(r'sair/', LogoutView.as_view(),  name='logout'),
	url(r'cadastrar_se', views.register, name='register')

	]