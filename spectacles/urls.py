from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # User Auth
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # Examples:
    url(r'^$', 'spectacles.views.home', name='home'),
    url(r'^geneset/', 'spectacles.views.geneset_view',name='geneset'),

    url(r'^admin/', include(admin.site.urls)),
)
