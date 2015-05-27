#coding=utf-8
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.template.context import RequestContext
from django.http.response import Http404, HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from cgi import valid_boundary
from django.contrib.auth import login,authenticate,logout
from django.contrib.admin.templatetags.admin_list import items_for_result
from MAIN.models import first_page_model, product_category_model,product_detail_model, product_picture_model
from WX.models import Response_By_Keywords_Model
from MANG.forms import First_Page_Model_Form_Add,First_Page_Model_Form_Edit,Product_Category_Model_Form,Product_Detail_Model_Form_Add,Product_Detail_Model_Form_Edit,\
    Product_Picture_Model_Form_Add,Product_Picture_Model_Form_Edit,\
    Response_By_Keywords_Model_Form_Add,Response_By_Keywords_Model_Form_Edit,Login_Form,Login_Form_Require
from MANG.decorator import is_superuser
#login page
class Login_Page(View):
    template='management_login.html'
    def get(self,request):
        form=Login_Form({'username':'','password':''})   #第一次显示表单是加入空白信息
        return render_to_response(self.template,{'form':form},RequestContext(request))
    def post(self,request):
        form=Login_Form_Require(request.POST)   #此时使用的表单需要用户名和密码
        if form.is_valid():                     #在表单的valid方法中验证用户名和密码是否有效
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)  #已经在form中验证过用户的存在了，在此处不需要在此验证了
            login(request,user)
            return HttpResponseRedirect(reverse('base_page')) 
        else:
            return render_to_response(self.template,{'form':form},RequestContext(request))
#logout page
class Logout_Page(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    def post(self,request):
        raise Http404   
# Create your views here.

class Base_Page(View):
    template='management_base.html'
    @is_superuser
    def get(self,request):
        return render_to_response(self.template,{},RequestContext(request))
    @is_superuser
    def post(self,request):
        return Http404  


class First_Page_Picture_Page(View):
    template_list='management_first_page_picture_list.html'
    template_add='management_first_page_picture_add.html'
    template_edit='management_first_page_picture_edit.html'
    @is_superuser
    def get(self,request,id=-1,todo='list'):
        if todo=='add': #add will load a new page ,list and delete option was on this page
            form=First_Page_Model_Form_Add(instance=first_page_model())
            return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit':
            mod=first_page_model.objects.get(pk=id)
            form=First_Page_Model_Form_Edit(instance=mod)
            return render_to_response(self.template_edit,{'form':form,'id':id},RequestContext(request))
        #default options,list the item
        first_page_picture_list=first_page_model.objects.all()
        return render_to_response(self.template_list,{'first_page_picture_list':first_page_picture_list},RequestContext(request))
    @is_superuser
    def post(self,request,id=-1,todo='list'):
        if todo=='add': # the add page
            form= First_Page_Model_Form_Add(request.POST,request.FILES)
            if form.is_valid(): #格式正确
                form.save() #save date to database
                return HttpResponseRedirect(reverse('first_page_picture_list'))
            else:  #上传格式错误
                return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit': #edit the item 
            pre=first_page_model.objects.get(pk=id)
            form= First_Page_Model_Form_Edit(request.POST,request.FILES,instance=pre)#this may cause a error
            if form.is_valid(): #the user change the upload file
                form.save()
                return HttpResponseRedirect(reverse('first_page_picture_list'))
            else:#the user my not change the file or realy invalid
                return render_to_response(self.template_edit,{'form':form,'id':id},RequestContext(request))
        #other is delete or edit options
        if request.POST['action']=='delete':
            list= request.POST.getlist('items')
            self.deleteItemInDatabaseByList(list) #this is utf8 char list be carefull
            return HttpResponseRedirect(reverse('first_page_picture_list'))
        if request.POST['action']=='edit':
            list=request.POST.getlist('items')
            if len(list)==0: #if nothing was select
                return HttpResponseRedirect(reverse('first_page_picture_list'))
            id=int(list[0])
            return HttpResponseRedirect(reverse('first_page_picture_edit',args=[id]))
    def deleteItemInDatabaseByList(self,list):
        for i in list:
            item=first_page_model.objects.get(pk=int(i))
            item.delete()


class Category_Page(View):
    template='category_setting_page.html'
    @is_superuser
    def get(self,request):
        #Product_Category_Model_Form_Set=modelformset_factory(Product_Category_Model_Form)
        Product_Category_Model_Form_Set=modelformset_factory(product_category_model,form=Product_Category_Model_Form,max_num=5)

        #init_data=[{'category_name':'1'},{'category_name':'2'}]
        ##
        category_list=product_category_model.objects.all()
        if len(category_list)!=5: # empty category list,init it first
            for i in [1,2,3,4,5]:
                empty_item=product_category_model(category_name=u'未设置')
                empty_item.save()
        formset=Product_Category_Model_Form_Set(queryset=product_category_model.objects.all())
        return render_to_response(self.template,{'formset':formset},RequestContext(request))
    @is_superuser
    def post(self,request):
        Product_Category_Model_Form_Set=modelformset_factory(product_category_model,form=Product_Category_Model_Form)
        formset=Product_Category_Model_Form_Set(request.POST)
        if formset.is_valid():
            formset.save()
            print "valid"
            return HttpResponseRedirect(reverse('category_setting'))
        else:
            print "invalid"
            return render_to_response(self.template,{'formset':formset},RequestContext(request))


class Product_Page(View):
    template_list='management_product_detail_list.html'
    template_add='management_product_detail_add.html'
    template_edit='management_product_detail_edit.html'
    @is_superuser
    def get(self,request,id=-1,todo='list'):
        if todo=='add':
            form=Product_Detail_Model_Form_Add(instance=product_detail_model())
            return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit':
            product=product_detail_model.objects.get(pk=id)
            form=Product_Detail_Model_Form_Edit(instance=product)
            return render_to_response(self.template_edit,{'form':form,'id':id},RequestContext(request))
        #if not add or edit ,just list all
        product_detail_list=product_detail_model.objects.all()
        return render_to_response(self.template_list,{'product_detail_list':product_detail_list},RequestContext(request))
    @is_superuser
    def post(self,request,id=-1,todo='list'):
        if todo=='add':
            form=Product_Detail_Model_Form_Add(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('product_detail_list'))
            else: #invalid form for add item
                return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit':
            pre=product_detail_model.objects.get(pk=id)
            form=Product_Detail_Model_Form_Edit(request.POST,request.FILES,instance=pre)
            if form.is_valid():
                #print form.cleaned_data
                #print 'edit valid'
                form.save()
                return HttpResponseRedirect(reverse('product_detail_list'))
            else: #invalid form for add item
                #print 'edit invalid'
                return render_to_response(self.template_edit,{'form':form},RequestContext(request))
        #hander ths edit of delete options
        if request.POST['action']=='edit': #choice a select item and redict to detail edit page
            #print "actions:%s" %(request.POST['action'])
            list=request.POST.getlist('items')
            if len(list)==0: #if nothing was select
                return HttpResponseRedirect(reverse('product_detail_list'))
            id=int(list[0])
            return HttpResponseRedirect(reverse('product_detail_edit',args=[id]))
        if request.POST['action']=='delete': #delete the selected items_for_result
            list=request.POST.getlist('items')
            self.deleteItemInDatabaseByList(list) #this is utf8 char list be carefull
            return HttpResponseRedirect(reverse('product_detail_list'))
    def deleteItemInDatabaseByList(self,list):
        for i in list:
            item=product_detail_model.objects.get(pk=int(i))
            item.delete()
            

class Product_Picture_Page(View):
    template_list='management_product_picture_list.html'
    template_add='management_product_picture_add.html'
    template_edit='management_product_picture_edit.html'
    @is_superuser
    def get(self,request,id=-1,todo='list'):
        if todo=='add':  #add method
            instance=product_picture_model()
            form=Product_Picture_Model_Form_Add(instance=instance)
            return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit': #edit method
            instance=product_picture_model.objects.get(pk=id)
            form=Product_Picture_Model_Form_Edit(instance=instance)
            return render_to_response(self.template_edit,{'form':form},RequestContext(request))
        #list all product picture
        product_picture_list=product_picture_model.objects.all()
        return render_to_response(self.template_list,{'product_picture_list':product_picture_list},RequestContext(request))
    @is_superuser
    def post(self,request,id=-1,todo='list'):
        if todo=='add':
            form=Product_Picture_Model_Form_Add(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('product_picture_list'))
            else:  #invalid
                return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit':
            pre=product_picture_model.objects.get(pk=id)
            form=Product_Picture_Model_Form_Edit(request.POST,request.FILES,instance=pre)
            if form.is_valid():
                print "valid"
                form.save()
                return HttpResponseRedirect(reverse('product_picture_list'))
            else:  #invalid
                print "invalid"
                return render_to_response(self.template_edit,{'form':form},RequestContext(request))
        #delete or edit item
        if request.POST['action']=='edit': #choice a select item and redict to detail edit page
            list=request.POST.getlist('items')
            if len(list)==0: #if nothing was select
                return HttpResponseRedirect(reverse('product_picture_list'))
            id=int(list[0])
            return HttpResponseRedirect(reverse('product_picture_edit',args=[id]))
        if request.POST['action']=='delete': #delete the selected items_for_result
            list=request.POST.getlist('items')
            self.deleteItemInDatabaseByList(list) #this is utf8 char list be carefull
            return HttpResponseRedirect(reverse('product_picture_list'))
    def deleteItemInDatabaseByList(self,list):
        for i in list:
            item=product_picture_model.objects.get(pk=int(i))
            item.delete()   
            

class Weixin_Response_By_Keywords_Page(View):
    template_list='management_weixin_response_by_keywords_list.html'
    template_add='management_weixin_response_by_keywords_add.html'
    template_edit='management_weixin_response_by_keywords_edit.html'
    @is_superuser
    def get(self,request,id=-1,todo='list'):
        if todo=='add':
            form=Response_By_Keywords_Model_Form_Add(instance=Response_By_Keywords_Model())
            return render_to_response(self.template_add,{'form':form},RequestContext(request))
        if todo=='edit':
            instance=Response_By_Keywords_Model.objects.get(pk=id);
            form=Response_By_Keywords_Model_Form_Edit(instance=instance);
            return render_to_response(self.template_edit,{'form':form,'id':id},RequestContext(request))
        
        #this means list all the item
        keywords_list=Response_By_Keywords_Model.objects.all()
        print "Number item in list",keywords_list.count()
        return render_to_response(self.template_list,{'keywords_list':keywords_list},RequestContext(request))
    @is_superuser
    def post(self,request,id=-1,todo='list'):
        if todo=='add':
            form=Response_By_Keywords_Model_Form_Add(request.POST)
            if form.is_valid():
                print "valid"
                form.save()
                return HttpResponseRedirect(reverse('weixin_response_by_keywords_list'))
            else:
                print "invalid"
                return render_to_response(self.template_add, {'form':form},RequestContext(request))        
        if todo=='edit':
            pre=Response_By_Keywords_Model.objects.get(pk=id)
            form=Response_By_Keywords_Model_Form_Edit(request.POST,instance=pre)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('weixin_response_by_keywords_list'))
            else:  #invalid
                return render_to_response(self.template_edit,{'form':form},RequestContext(request))
        #delete or edit item
        if request.POST['action']=='edit': #choice a select item and redict to detail edit page
            list=request.POST.getlist('items')
            if len(list)==0: #if nothing was select
                return HttpResponseRedirect(reverse('weixin_response_by_keywords_list'))
            id=int(list[0])
            return HttpResponseRedirect(reverse('weixin_response_by_keywords_edit',args=[id]))
        if request.POST['action']=='delete': #delete the selected items_for_result
            list=request.POST.getlist('items')
            self.deleteItemInDatabaseByList(list) #this is utf8 char list be carefull
            return HttpResponseRedirect(reverse('weixin_response_by_keywords_list'))
    def deleteItemInDatabaseByList(self,list):
        for i in list:
            item=Response_By_Keywords_Model.objects.get(pk=int(i))
            item.delete()  