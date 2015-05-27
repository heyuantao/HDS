from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


from WX.views import Process

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HDS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/$', Process.as_view()),
)
