#coding=utf-8
from django.forms import ModelForm,Form
from django.forms.formsets import formset_factory
from django import forms
from django.db import models
from MAIN.models import first_page_model,product_category_model,product_detail_model,product_picture_model
from WX.models import Response_By_Keywords_Model
from django.contrib.auth import authenticate

class Login_Form(Form): #this form is use for user input username and password
    username=forms.CharField(error_messages={'required': u'请输入用户名'},required=False)
    password=forms.CharField(error_messages={'required': u'请输入密码'},required=False)
    def clean(self):
        cleaned_data=super(Login_Form,self).clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        if self.login_auth(username,password):
            return cleaned_data #用户认证成功
        else:
            raise forms.ValidationError("用户名不存在或者密码错误！")   #用户认证失败
    def login_auth(self,username,password):
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                return True
            else:
                return False
        return False
    #def get_username(self):
    #    return self.username
    
class Login_Form_Require(Login_Form):   #当用户提及数据是使用次表单
    username=forms.CharField(error_messages={'required': u'请输入用户名'},required=True)
    password=forms.CharField(error_messages={'required': u'请输入密码'},required=True)
    
class First_Page_Model_Form_Add(ModelForm):
    class Meta:
        model=first_page_model
        fields='__all__'
    name = forms.CharField(error_messages={'required': u'填写图片名称'})
    image = forms.ImageField(error_messages={'required':u'请指定上传图片'})
    image = forms.ImageField(required=True)
    
class First_Page_Model_Form_Edit(ModelForm):    
    class Meta:
        model=first_page_model
        fields='__all__'
    name = forms.CharField(error_messages={'required': u'填写图片名称'})
    image = forms.ImageField(error_messages={'required':u'请指定上传图片'})
    image = forms.ImageField(required=False)
    
class Product_Category_Model_Form(ModelForm):
    class Meta:
        model=product_category_model
        fields='__all__'
    category_name = forms.CharField(error_messages={'required':u'必须填写产品类别信息'})
    
class Product_Detail_Model_Form_Add(ModelForm):
    front_picture=forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=True)
    back_picture=forms.ImageField(error_messages={'required':u'请指定上传背景图片'},required=True)
    class Meta:
        model=product_detail_model
        fields='__all__'
    
    
class Product_Detail_Model_Form_Edit(ModelForm):
    front_picture=forms.ImageField(error_messages={'required':u'请指定上前景传图片'},required=False)
    back_picture=forms.ImageField(error_messages={'required':u'请指定上传背景图片'},required=False)
    class Meta:
        model=product_detail_model
        fields='__all__'
 
class Product_Picture_Model_Form_Add(ModelForm):   
    info1_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=True)
    info2_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=True)
    info3_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=True)
    class Meta:
        model=product_picture_model
        fields='__all__'

class Product_Picture_Model_Form_Edit(ModelForm):   
    info1_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=False)
    info2_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=False)
    info3_picture = forms.ImageField(error_messages={'required':u'请指定上传前景图片'},required=False)
    class Meta:
        model=product_picture_model
        fields='__all__'
        
class Response_By_Keywords_Model_Form_Add(ModelForm): #use edit 
    keywords=forms.CharField(error_messages={'required':u'请输入关键字，并以分号（英文）分隔'},required=True)
    response=forms.CharField(error_messages={'required':u'请输入关键字，并以分号（英文）分隔'},required=True)
    class Meta:
        model=Response_By_Keywords_Model
        fields='__all__'
    def clean_keywords(self):
        data=self.cleaned_data['keywords']
        data_splited=data.split(';')
        for word in data_splited:
            print word
            if (u';' in word) or (u',' in word) or  (u'，' in word):
                raise forms.ValidationError(u'关键字必须以英文冒号隔开!')   
        return data
    
class Response_By_Keywords_Model_Form_Edit(Response_By_Keywords_Model_Form_Add):
    pass