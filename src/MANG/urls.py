from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from MAIN.views import Home_Page,AboutUs_Page,ContactUs_Page,Products_Page,Index_Page
from MANG.views import Base_Page,First_Page_Picture_Page,Category_Page,Product_Page,Product_Picture_Page,Weixin_Response_By_Keywords_Page,\
    Login_Page,Logout_Page

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HDS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #login page
    url(r'^login/', Login_Page.as_view(),name='login'),
    url(r'^logout/', Logout_Page.as_view(),name='logout'),
    #### management page
    url(r'^base_page/', Base_Page.as_view(),name='base_page'),
    url(r'^first_page_picture/add/$', First_Page_Picture_Page.as_view(),{'todo':'add'},name='first_page_picture_add'),
    url(r'^first_page_picture/(?P<id>\d+)/$', First_Page_Picture_Page.as_view(),{'todo':'edit'},name='first_page_picture_edit'),
    url(r'^first_page_picture/$', First_Page_Picture_Page.as_view(),{'todo':'list'},name='first_page_picture_list'),
    
    url(r'^category/', Category_Page.as_view(),name='category_setting'),

    url(r'^product_detail/add/$', Product_Page.as_view(),{'todo':'add'},name='product_detail_add'),
    url(r'^product_detail/edit/(?P<id>\d+)/$', Product_Page.as_view(),{'todo':'edit'},name='product_detail_edit'),
    url(r'^product_detail/$', Product_Page.as_view(),{'todo':'list'},name='product_detail_list'),
    
    url(r'^product_picture/add/$', Product_Picture_Page.as_view(),{'todo':'add'},name='product_picture_add'),
    url(r'^product_picture/edit/(?P<id>\d+)/$', Product_Picture_Page.as_view(),{'todo':'edit'},name='product_picture_edit'),
    url(r'^product_picture/$', Product_Picture_Page.as_view(),{'todo':'list'},name='product_picture_list'),
    
    
    url(r'^weixin_respon_by_keywords/add/$', Weixin_Response_By_Keywords_Page.as_view(),{'todo':'add'},name='weixin_response_by_keywords_add'),
    url(r'^weixin_respon_by_keywords/edit/(?P<id>\d+)/$', Weixin_Response_By_Keywords_Page.as_view(),{'todo':'edit'},name='weixin_response_by_keywords_edit'),
    url(r'^weixin_respon_by_keywords/$', Weixin_Response_By_Keywords_Page.as_view(),{'todo':'list'},name='weixin_response_by_keywords_list'),
    # url(r'^login/', include('WX.urls')),
    # url(r'^login/', include('WX.urls')),
)