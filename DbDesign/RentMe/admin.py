from django.contrib import admin
from .models import *
# Register your models here.

#车型信息
class model_infoAdmin(admin.ModelAdmin):
    list_display = ('car_model_id',)
    list_filter = ('car_type','car_brand','car_issue_date',)

#车辆信息
class car_infoAdmin(admin.ModelAdmin):
    list_display = ('car_num',)

#管理员信息
class admin_infoAdmin(admin.ModelAdmin):
    list_display = ('admin_name',)

#门店信息
class store_infoAdmin(admin.ModelAdmin):
    list_display = ('store_id',)

#用户信息
class user_infoAdmin(admin.ModelAdmin):
    list_display = ('user_name',)

#租车订单信息
class rent_orderAdmin(admin.ModelAdmin):
    list_display = ('order_id',)

#租车记录信息
class relet_recordAdmin(admin.ModelAdmin):
    list_display = ('relet_id',)

#违章信息
class illegal_recordAdmin(admin.ModelAdmin):
    list_display = ('illegal_id',)

#驾驶证信息
class driving_licenseAdmin(admin.ModelAdmin):
    list_display = ('user_drive',)

admin.site.register(model_info,model_infoAdmin)
admin.site.register(car_info,car_infoAdmin)
admin.site.register(store_info,store_infoAdmin)
admin.site.register(user_info,user_infoAdmin)
admin.site.register(admin_info,admin_infoAdmin)
admin.site.register(rent_order,rent_orderAdmin)
admin.site.register(relet_record,relet_recordAdmin)
admin.site.register(illegal_record,illegal_recordAdmin)
admin.site.register(driving_license,driving_licenseAdmin)
