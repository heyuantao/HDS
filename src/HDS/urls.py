from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from MAIN.views import Home_Page,AboutUs_Page,ContactUs_Page,Products_Page,ProductDetail_Page,Index_Page

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HDS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^weixin/', include('WX.urls')),
    url(r'^home/',Home_Page.as_view(),name='home'),
    url(r'^about_us/',AboutUs_Page.as_view(),name='about_us'),
    url(r'^products_category/(?P<type_id>\d+)/(?P<current_page>\d+)$',Products_Page.as_view(),name='products_category_with_type'),
    url(r'^products_category/$',Products_Page.as_view(),name='products_category'),   
    url(r'^contact_us/',ContactUs_Page.as_view(),name='contact_us'),
    url(r'^product_detail/(?P<id>\d+)/$',ProductDetail_Page.as_view(),name='product_detail'),
    url(r'^$',Index_Page.as_view(),name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/',include('MANG.urls')),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
