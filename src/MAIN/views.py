#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.template.context import RequestContext
from django.http.response import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from MAIN.models import first_page_model,product_category_model,product_detail_model,\
    product_picture_model
from django.core.urlresolvers import reverse
# Create your views here.

class Home_Page(View):
    template='home.html'
    def get(self,request):
        first_page_pics=first_page_model.objects.all()
        product_to_show=product_detail_model.objects.filter(display_on_first_page=True)[0:4] #max item is four
        page_context={'first_page_pics':first_page_pics,'product_to_show':product_to_show}
        return render_to_response(self.template,page_context,RequestContext(request));
    def post(self,request):
        raise Http404
    
class AboutUs_Page(View):
    template='about_us.html'
    def get(self,request):
        page_context={}
        return render_to_response(self.template,page_context,RequestContext(request));
    def post(self,request):
        raise Http404
    
class Products_Page(View):
    template='products_category.html'
    def get(self,request,type_id=-1,current_page=1):
        if type_id==-1:   #如果没有id，则将id设置为第一类商品，这样避免数据库查询出错
            type_id=product_category_model.objects.all()[0].id
        product_type_list=product_category_model.objects.all()[0:5]  #产品详情页只能显示5类商品，多了就不显示了
        #all_product_detail=product_detail_model.objects.all()
        special_product_detail=product_detail_model.objects.filter(category__pk=type_id)
        #product_detail_list_with_page=Paginator(all_product_detail,10)
        product_detail_list_with_page=Paginator(special_product_detail,10)
        product_detail_page=product_detail_list_with_page.page(current_page)
        #print product_detail_page.number
        page_context={'product_type_list':product_type_list,'product_detail_page':product_detail_page}
        #page_context['page_number']=product_detail_list_with_page.num_pages
        #page_context['current_page']=current_page
        page_context['type_id']=type_id
        return render_to_response(self.template,page_context,RequestContext(request));
    def post(self,request):
        raise Http404
    
class ContactUs_Page(View):
    template='contact_us.html'
    def get(self,request):
        page_context={}
        return render_to_response(self.template,page_context,RequestContext(request));
    def post(self,request):
        raise Http404
    
class ProductDetail_Page(View):
    template='product_detail.html'
    def get(self,request,id):
        try:
            product_type_list=product_category_model.objects.all()
            product_item=product_detail_model.objects.get(pk=id)
            page_context={'product_type_list':product_type_list,'product_item':product_item}
            #print product_item.title            
        except Exception:
            raise Http404
        return render_to_response(self.template,page_context,RequestContext(request));
    def post(self,request):
        raise Http404

class Index_Page(View):
    def get(self,request):
        return HttpResponseRedirect(reverse('home'))
    def post(self,request):
        raise Http404