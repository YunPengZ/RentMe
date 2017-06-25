from rest_framework import serializers
from RentMe.models import driving_license


class DrivingSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user_drive = serializers.CharField(required=False,allow_blank=True,max_length=12)
    drive_type = serializers.CharField(required=False,default='C级驾照',max_length=12)
    drive_age = serializers.IntegerField()
    drive_start_date = serializers.DateField()
    drive_end_date = serializers.DateField()

    def create(self, validated_data):
        #数据合法，返回并创建driving_license实例
        return driving_license.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_drive = validated_data.get('user_drive',instance.user_drive)
        instance.drive_type = validated_data.get('user_drive',instance.user_drive)
        instance.drive_age = validated_data.get('user_drive',instance.user_drive)
        instance.drive_start_date = validated_data.get('drive_start_date',instance.drive_start_date)
        instance.drive_end_date = validated_data.get('drive_end_date',instance.drive_end_date)
        instance.save()
        return instance
