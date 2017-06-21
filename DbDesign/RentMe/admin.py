from django.contrib import admin
from .models import *
# Register your models here.

class model_infoAdmin(admin.ModelAdmin):
    list_display = ('car_model_id',)
    list_filter = ('car_type',)

class car_infoAdmin(admin.ModelAdmin):
    list_display = ('car_num',)

class admin_infoAdmin(admin.ModelAdmin):
    list_display = ('admin_num',)

class store_infoAdmin(admin.ModelAdmin):
    list_display = ('store_num',)

class user_infoAdmin(admin.ModelAdmin):
    list_display = ('user_num',)

class rent_orderAdmin(admin.ModelAdmin):
    list_display = ('order_num',)

class relet_recordAdmin(admin.ModelAdmin):
    list_display = ('relet_id',)

class illegal_recordAdmin(admin.ModelAdmin):
    list_display = ('illegal_id',)

admin.site.register(model_info,model_infoAdmin)
admin.site.register(car_info,car_infoAdmin)
admin.site.register(store_info,store_infoAdmin)
admin.site.register(user_info,user_infoAdmin)
admin.site.register(admin_info,admin_infoAdmin)
admin.site.register(rent_order,rent_orderAdmin)
admin.site.register(relet_record,relet_recordAdmin)
admin.site.register(illegal_record,illegal_recordAdmin)