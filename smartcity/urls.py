from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'smartcity.views.home', name='home'),
     url(r'', include('xena.urls',namespace="xena")),

    url(r'^admin/', include(admin.site.urls)),
]
