#from django.contrib.auth import login
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView

app_name = 'Accounts'

urlpatterns = [
	#url(r'^entrar/', include('django.contrib.auth.urls'),
	 #{'template_name': 'accounts/login.html'}, name='login'),
	url(r'^entrar/', LoginView.as_view(), 
	{'template_name': 'accounts/login.html'}, name='login'),

	]