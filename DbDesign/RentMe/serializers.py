# coding:utf-8
from rest_framework import serializers
from rest_framework.serializers import *
from RentMe.models import *

#关联Model_info
class ModelSerializer(serializers.ModelSerializer):
    car_model = serializers.PrimaryKeyRelatedField(many=True, queryset=car_info.objects.all())
    class Meta:
        model = model_info
        #DELETED : 'car_record_create_time'
        fields = ('model_id','car_model','car_model_id','car_type','car_brand','car_series','car_issue_date','car_config_model','car_seats_num','car_doors','car_fuel_type','car_gearbox_type','car_displacement','car_fuel_num','car_drive_way','car_engine_intake','car_skylight','car_tank_capa','car_voicebox','car_seats_type','car_reverse_radar','car_airbag','car_dvd','car_gps','car_deposit','car_day_price','car_time_out_price','car_over_kilo_price','record_delete_status')
#关联user_info
class UserSerializer(serializers.ModelSerializer):
    user_rent = serializers.PrimaryKeyRelatedField(many=True,queryset=rent_order.objects.all())

    class Meta:
        model = user_info
        fields = ('user_id','user_name','user_rent','user_sex','user_age','user_ident','user_tel','user_office','user_addr','user_post','user_email','user_record_create_time','record_delete_status','record_create_admin')
#关联admin_info
class AdminSerializer(serializers.ModelSerializer):
    #store_manage = serializers.HyperlinkedRelatedField(many=True,view_name='adminn-detail',read_only=True)
    class Meta:
        model = admin_info
        fields = ('admin_id','admin_tel','admin_pas','admin_name','store_manage','admin_sex','admin_age','admin_type','admin_email','admin_ident',)
#关联car_info
class CarSerializer(serializers.ModelSerializer):
    car_model_id = serializers.PrimaryKeyRelatedField(many=True, queryset=model_info.objects.all())
    class Meta:
        model = car_info
        fields = ('car_id','car_num','car_model_id','car_color','car_engine_num','car_frame_num','car_buy_date','car_retailer','car_status','car_ins_num','car_record_create_time','record_create_admin','record_delete_status')
#关联 user_info
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = user_info
#         #DELETED ,'user_record_create_time'
#         fields = ('user_id','user_name','user_sex','user_age','user_ident','user_tel','user_office','user_addr','user_post','user_email','record_create_admin','user_record_create_time','record_delete_status')
#关联 driving_license
class DrivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = driving_license
        fields = ('drive_id','user_drive','drive_type','drive_age','drive_name','drive_start_date','drive_end_date')
#关联store_info
class StoreSerializer(serializers.ModelSerializer):
    #store_admin = serializers.ReadOnlyField(source='store_admin.admin_name')
    class Meta:
        model = store_info
        fields = ('store_id','store_addr','store_tel','store_start_time','store_admin','store_record_create_time','record_delete_status')
#关联car_info
class CarSerializer(serializers.ModelSerializer):
   # car_model_id = serializers.ReadOnlyField(source='car_model_id.model_id')
    class Meta:
        model =car_info
        fields = ('car_id','car_num','car_model_id','car_color','car_engine_num','car_engine_num','car_frame_num','car_buy_date','car_retailer','car_status','car_ins_num','record_create_admin','car_record_create_time','record_delete_status')
#关联rent_order
class OrderSerializer(serializers.ModelSerializer):
    relet_order = serializers.PrimaryKeyRelatedField(many=True,queryset=relet_record.objects.all())
    class Meta:
        model = rent_order
        fields = ('order_id','relet_order','user_num','car_num','user_drive','pick_addr','pick_time','drop_time','actual_deposit','breaken_bill','illegal_info','illegal_bill','actual_money','record_create_admin','order_record_create_time','record_delete_status')
#关联relet_record
class ReletSerializer(serializers.ModelSerializer):
    class Meta:
        model = relet_record
        fields = ('relet_id','order_num','relet_start_time','record_create_admin','relet_record_create_time','record_delete_status')
#关联illegal_record
class illegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = illegal_record
        fields = ('illegal_id','illegal_car_num','illegal_date','illegal_bill','illegal_info','illegal_record_create_time','record_create_admin','record_delete_status')

#class DrivingSerializer(serializers.Serializer):
    #pk = serializers.IntegerField(read_only=True)
   # user_drive = serializers.CharField(required=False,allow_blank=True,max_length=12)
    #drive_type = serializers.CharField(required=False,default='C级驾照',max_length=12)
    #drive_age = serializers.IntegerField()
    #drive_start_date = serializers.DateField()
    #drive_end_date = serializers.DateField()

    #def create(self, validated_data):
        #数据合法，返回并创建driving_license实例
       # return driving_license.objects.create(**validated_data)

    #def update(self, instance, validated_data):
        #instance.user_drive = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_type = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_age = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_start_date = validated_data.get('drive_start_date',instance.drive_start_date)
        #instance.drive_end_date = validated_data.get('drive_end_date',instance.drive_end_date)
        #instance.save()
       # return instance
        #fields = ('admin_id','admin_tel','admin_pas','admin_name','store_manage','admin_sex','admin_age','admin_record_create_time','admin_type','admin_email','admin_ident',)
