from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^make/', include('make.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^wiki/(?P<page_title>[^/]+)/$', 'make.wiki.views.view_page'),
	(r'^wiki/(?P<page_title>[^/]+)/edit/$', 'make.wiki.views.edit_page'),
	(r'^wiki/(?P<page_title>[^/]+)/save/$', 'make.wiki.views.save_page'),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^blog/(?P<post_title>[^/]+)/$', 'make.blog.views.view_post'), 
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    
)
