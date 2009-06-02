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
    (r'^$', 'make.home.index'),
)

urlpatterns += patterns('make.projects.views',
    (r'^projects/$', 'index'),
    (r'^projects/new/$', 'create_project'),
    (r'^projects/(?P<project_title>[^/]+)/$', 'view_project'),
    (r'^projects/(?P<project_title>[^/]+)/edit/$', 'edit_project'),
)

urlpatterns += patterns('make.wiki.views',
    (r'^wiki/$', 'index'),
    (r'^wiki/new/$', 'create_page'),
    (r'^wiki/(?P<page_title>[^/]+)/$', 'view_page'),
    (r'^wiki/(?P<page_title>[^/]+)/edit/$', 'edit_page'),
    (r'^wiki/(?P<page_title>[^/]+)/save/$', 'save_page'),
    (r'^wiki/(?P<page_title>[^/]+)/history/$', 'page_history'),
)

urlpatterns += patterns('make.forum.views',
    (r'^forum/$' , 'index'),
    (r'^forum/(?P<category_title>[^/]+)/$' , 'category'),
	(r'^forum/(?P<category_title>[^/]+)/(?P<thread_title>[^/]+)/$', 'thread'),
)        

urlpatterns += patterns('make.blog.views',
    (r'^blog/$', 'index'), 
    (r'^blog/new/$', 'create_post'), 
	(r'^blog/save/$', 'save_post'), 
    (r'^blog/(?P<post_title>[^/]+)/$', 'view_post'), 
    (r'^blog/(?P<post_title>[^/]+)/edit/$', 'edit_post'), 
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/create/$', 'make.member.views.create_profile'),
    (r'^accounts/profile/$', 'make.member.views.self_profile'),
    (r'^profile/(?P<username>[^/]+)/$', 'make.member.views.profile'),
    (r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
    (r'^search/', include('haystack.urls')),
)
