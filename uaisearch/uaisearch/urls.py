from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uaisearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', include('uai_search_web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
