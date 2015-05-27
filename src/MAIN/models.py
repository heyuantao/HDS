#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class first_page_model(models.Model):
    class Meta:
        verbose_name_plural=u'首页设置（图片）'
        verbose_name=u'图片设置'
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='upload_images',null=True, blank=True)
    link_to = models.TextField(blank=True)
    def __unicode__(self):
        return u"%s" %(self.name)
        
class product_category_model(models.Model):
    class Meta:
        verbose_name_plural=u'产品（挂面）整体分类'
        verbose_name=u'分类详情'
    category_name = models.CharField(max_length=50)
    def __unicode__(self):
        return "%s" %(self.category_name)
 
class product_picture_model(models.Model):   
    class Meta:
        verbose_name_plural=u'产品（挂面）广告图片'
        verbose_name=u'图片设置'
    #product = models.ForeignKey(product_detail_model)     
    name = models.CharField(max_length=30)
    info1_picture = models.ImageField(upload_to='upload_images')
    info2_picture = models.ImageField(upload_to='upload_images')
    info3_picture = models.ImageField(upload_to='upload_images')
    def __unicode__(self):
        return "product name is %s" %(self.name)  
    
class product_detail_model(models.Model):
    class Meta:
        verbose_name_plural=u'产品（挂面）详情信息'
        verbose_name=u'产品信息'
    title = models.CharField(max_length=50)
    category = models.ForeignKey(product_category_model)    
    net_content = models.IntegerField()
    warranty_period = models.IntegerField()
    nutritive_index = models.TextField(blank=True)
    ingredient = models.TextField(blank=True)
    preservation_method = models.TextField(blank=True)
    front_picture = models.ImageField(upload_to='upload_images',null=True, blank=True)
    back_picture = models.ImageField(upload_to='upload_images',null=True, blank=True)
    product_pic =models.ForeignKey(product_picture_model)
    display_on_first_page = models.BooleanField(default=False)
    def __unicode__(self):
        return "Product:%s belong to:%s \t net_content:%s" %(self.title,self.category.category_name,self.net_content)
    
class site_info_model(models.Model):
    class Meta:
        verbose_name_plural=u'站点专有数据设置'
        verbose_name=u'设置'
    key = models.CharField(max_length=50)
    value = models.TextField()
    picture = models.ImageField(upload_to='upload_images',max_length=255)
    def __unicode__(self):
        return "Key:%s and Value is %s" %(self.key,self.value)