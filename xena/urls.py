from django.conf.urls import url
from .import views


urlpatterns = [
	url(r'^$',views.log_in,name='login'),
	url(r'^signup/$',views.sign_up,name='signup'),
	url(r'^home/$',views.home,name='home'),
	url(r'^logout/$',views.log_out,name = 'logout'),
	url(r'^user/$',views.info_save,name = 'infosave'),
	url(r'^user_E/$',views.info_fill,name = "infofill"),
]
