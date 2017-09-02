from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^logout/$',auth_views.logout,{'next_page':'/'},name='logout'),
	url(r'^login/$',auth_views.login,{'template_name':'xena/login.html'},name='login'),
#	url(r'^$',views.log_in,name='login'),
	url(r'^signup/$',views.sign_up,name='signup'),
	url(r'^home/$',views.home,name='home'),
#	url(r'^logout/$',views.log_out,name = 'logout'),
	url(r'^user/$',views.info_save,name = 'infosave'),
	url(r'^user_E/$',views.info_fill,name = "infofill"),
	url(r'^comment_save/$',views.comment_save,name="comment_save"),
	url(r'^view_save/$',views.view_save, name="view_save"),
	url(r'^query/$',views.query,name="query")
]
