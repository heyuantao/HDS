from django.contrib import admin
from MAIN.models import first_page_model,product_category_model,\
        product_detail_model,product_picture_model,site_info_model

# Register your models here.

#admin.site.register(first_page_model)
class product_category_model_admin(admin.ModelAdmin):
    list_display=('category_name',)
    
admin.site.register(product_category_model,product_category_model_admin)

class product_detail_model_admin(admin.ModelAdmin):
    list_display=('title','category','net_content','warranty_period','nutritive_index','ingredient','display_on_first_page')
    
admin.site.register(product_detail_model,product_detail_model_admin)

admin.site.register(site_info_model)

class product_picture_model_admin(admin.ModelAdmin):
    list_display=('name','info1_picture','info2_picture','info3_picture')
admin.site.register(product_picture_model, product_picture_model_admin)
    
class first_page_model_admin(admin.ModelAdmin):
    list_display=('name','link_to','image')

admin.site.register(first_page_model, first_page_model_admin)