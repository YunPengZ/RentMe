# coding:utf-8
from rest_framework import serializers
from RentMe.models import *


class DrivingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = driving_license
        fields = ('drive_id','user_drive','drive_type','drive_age','drive_start_date','drive_end_date')

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    #store_manage = serializers.HyperlinkedRelatedField(many=True,view_name='adminn-detail',read_only=True)
    class Meta:
        model = admin_info
        fields = ('admin_id','admin_tel','admin_pas','admin_name','store_manage','admin_sex','admin_age','admin_record_create_time','admin_type','admin_email','admin_ident',)

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    #store_admin = serializers.ReadOnlyField(source='store_admin.admin_name')
    class Meta:
        model = store_info
        fields = ('store_id','store_addr','store_tel','store_start_time','store_admin','store_record_create_time','record_delete_status')

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =car_info
        field = ('car_id','car_num','car_model_id','car_color','car_engine_num','car_engine_num','car_fame_num','car_buy_date','car_retailer','car_status','car_ins_num','car_record_create_time','record_delete_status')


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
