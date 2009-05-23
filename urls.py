from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import haystack
haystack.autodiscover()


urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/kevindavenport/Documents/djangoprojects/make/media'}),
    (r'^wiki/(?P<page_title>[^/]+)/$', 'make.wiki.views.view_page'),
    (r'^wiki/(?P<page_title>[^/]+)/edit/$', 'make.wiki.views.edit_page'),
    (r'^wiki/(?P<page_title>[^/]+)/save/$', 'make.wiki.views.save_page'),
    (r'^forum/$' , 'make.forum.views.index'),
    (r'^forum/(?P<category_title>[^/]+)/$' , 'make.forum.views.category'),
	(r'^forum/(?P<category_title>[^/]+)/(?P<thread_title>[^/]+)/$', 'make.forum.views.thread'),
    (r'^comments/', include('django.contrib.comments.urls')),
#    (r'^blog/save/$', 'make.blog.views.save_post'), 
    (r'^blog/new/$', 'make.blog.views.create_post'), 
	(r'^blog/save/$', 'make.blog.views.save_post'), 
    (r'^blog/(?P<post_title>[^/]+)/$', 'make.blog.views.view_post'), 
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
#    (r'^accounts/create/&', 'make.member.views.create_account'),
    (r'^accounts/(?P<username>[^/]+)/$', 'make.member.views.profile'),
    (r'^accounts/(?P<username>[^/]+)/edit/$', 'make.member.views.edit_profile'),
    (r'^accounts/(?P<username>[^/]+)/save/$', 'make.member.views.save_profile'),
    (r'^search/', include('haystack.urls')),
)
