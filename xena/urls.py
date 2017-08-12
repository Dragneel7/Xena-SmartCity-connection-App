from django.conf.urls import url
from .import views


urlpatterns = [
	url(r'^$',views.log_in,name='login'),
	url(r'^signup/$',views.sign_up,name='signup'),
	url(r'^home/$',views.home,name='home'),
]
