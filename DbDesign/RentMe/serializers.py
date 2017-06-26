# coding:utf-8
from rest_framework import serializers
from RentMe.models import *


class DrivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = driving_license
        fields = ('drive_id','user_drive','drive_type','drive_age','drive_start_date','drive_end_date')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_info
        fields = ('admin_tel','admin_pas','admin_name','admin_sex','admin_age','admin_record_create_time','admin_type','admin_email','admin_ident',)

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
