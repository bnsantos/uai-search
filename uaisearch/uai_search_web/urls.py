__author__ = 'bruno'

from django.conf.urls import patterns, url

from uai_search_web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<search_input>\d+)/$', views.search, name='search'),
)