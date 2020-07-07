#from django.contrib.auth import login
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts import views



app_name = 'accounts'

urlpatterns = [
	#^$ para urls vazias e ^ para indicar a proxima url

	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^entrar/', LoginView.as_view(),  name='login'),
	url(r'^sair/', LogoutView.as_view(), name='logout'),
	url(r'^cadastrar_se', views.register, name='register'),
	url(r'^editar-senha', views.edit_password, name='edit_password'),
	url(r'^editar', views.edit, name='edit'),
	

	]