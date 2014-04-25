from django.conf.urls import patterns, include, url

from django.contrib import admin
from triWeb.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testPro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^$', index),
	(r'^dashboard/$',dashboard),
	(r'^assets/$', assets),
	(r'^status/$', getStatusData),
   
)


