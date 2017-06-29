# coding:utf-8
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from RentMe import models
from RentMe.serializers import *

#展示或者创建driving_license
#request.data 返回 字典包含前端传来的jason数据
#XXXX.objects.all.values()返回字典类型
#如果查询到多个记录时会以[dict(),dict(),……]的格式返回
#用 属性__in = []的方式来访问一个属性多个值匹配的情况
#filter(user_drive__in=['123456789','12345'])

#license_info查询&添加
@api_view(['GET','POST'])
def license_list(request=[],format=None):
    if request.method == 'GET':
        if len(request.data)==0:
            licenses = driving_license.objects.all()
            serializer = DrivingSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            licenses = driving_license.objects.all()
            if 'drive_id' in request_dict:
                licenses = licenses.filter(drive_id__in=request_dict['drive_id'])
            elif 'user_drive' in request_dict:
                licenses = licenses.filter(user_drive__in=request_dict['user_drive'])
            elif 'drive_type' in request_dict:
                licenses = licenses.filter(drive_type__in=request_dict['drive_type'])
            elif 'drive_age' in request_dict:
                licenses = licenses.filter(drive_age__in=request_dict['drive_age'])
            elif 'drive_name' in request_dict:
                licenses = licenses.filter(drive_name__in=request_dict['drive_name'])
            elif 'drive_start_date' in request_dict:
                licenses = licenses.filter(drive_start_date__in=request_dict['drive_start_date'])
            elif 'drive_end_date' in request_dict:
                licenses = licenses.filter(drive_end_date__in=request_dict['drive_end_date'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)

            serializer = DrivingSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)
    elif request.method == 'POST':
        request_dict = request.data
        print(request_dict)
        licenses = driving_license.objects.all()
        if 'drive_id' in request_dict:
            licenses = licenses.filter(drive_id__in=request_dict['drive_id'])
        elif 'user_drive' in request_dict:
            licenses = licenses.filter(user_drive__in=request_dict['user_drive'])
        elif 'drive_type' in request_dict:
            licenses = licenses.filter(drive_type__in=request_dict['drive_type'])
        elif 'drive_age' in request_dict:
            licenses = licenses.filter(drive_age__in=request_dict['drive_age'])
        elif 'drive_name' in request_dict:
            licenses = licenses.filter(drive_name__in=request_dict['drive_name'])
        elif 'drive_start_date' in request_dict:
            licenses = licenses.filter(drive_start_date__in=request_dict['drive_start_date'])
        elif 'drive_end_date' in request_dict:
            licenses = licenses.filter(drive_end_date__in=request_dict['drive_end_date'])
        elif 'record_delete_status' in request_dict:
            licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
        #print(licenses.values())
        licenses_list=list()
        for item in licenses.values():
            licenses_list.append(item)

        serializer = DrivingSerializer(data=licenses_list,many=True)
        if serializer.is_valid():
            return Response(serializer.data)
    '''if request.method == 'GET':
        licenses = driving_license.objects.all()
        licenses = licenses.filter(user_drive__in=['123456789','12345'])
        #for item in licenses.values():
        #    print(item)
        #print(licenses.values()[0])
        serializer = DrivingSerializer(licenses,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)'''

#illegal_record查询&添加
@api_view(['GET','POST'])
def illegal_list(request=[],format=None):
    if request.method == 'GET':
        licenses = illegal_record.objects.all()
        if len(request.data)==0:
            serializer = LllegalSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = illegal_record.objects.all()
            if 'illegal_id' in request_dict:
                licenses = licenses.objects.filter(illegal_id__in=request_dict['illegal_id'])
            elif 'illegal_car_num' in request_dict:
                licenses = licenses.filter(illegal_car_num__in=request_dict['illegal_car_num'])
            elif 'illegal_date' in request_dict:
                licenses = licenses.filter(illegal_date__in=request_dict['illegal_date'])
            elif 'illegal_bill' in request_dict:
                licenses = licenses.filter(illegal_bill__in=request_dict['illegal_bill'])
            elif 'illegal_info' in request_dict:
                licenses = licenses.filter(illegal_info__in=request_dict['illegal_info'])
            elif 'illegal_record_create_time' in request_dict:
                licenses = licenses.filter(illegal_record_create_time__in=request_dict['illegal_record_create_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = LllegalSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#car_info查询&添加
@api_view(['GET','POST'])
def car_list(request=[],format=None):
    if request.method == 'GET':
        licenses = car_info.objects.all()
        if len(request.data)==0:
            serializer = CarSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = car_info.objects.all()
            if 'car_id' in request_dict:
                licenses = licenses.objects.filter(car_id__in=request_dict['car_id'])
            elif 'car_num' in request_dict:
                licenses = licenses.filter(car_num__in=request_dict['car_num'])
            elif 'car_model_id' in request_dict:
                licenses = licenses.filter(car_model_id__in=request_dict['car_model_id'])
            elif 'car_color' in request_dict:
                licenses = licenses.filter(car_color__in=request_dict['ar_color'])
            elif 'car_engine_num' in request_dict:
                licenses = licenses.filter(car_engine_num__in=request_dict['car_engine_num'])
            elif 'car_frame_num' in request_dict:
                licenses = licenses.filter(car_frame_num__in=request_dict['car_frame_num'])
            elif 'car_buy_date' in request_dict:
                licenses = licenses.filter(car_buy_date__in=request_dict['car_buy_date'])
            elif 'car_retailer' in request_dict:
                licenses = licenses.filter(car_retailer__in=request_dict['car_retailer'])
            elif 'car_status' in request_dict:
                licenses = licenses.filter(car_status__in=request_dict['car_status'])
            elif 'car_ins_num' in request_dict:
                licenses = licenses.filter(car_ins_num__in=request_dict['car_ins_num'])
            elif 'car_record_create_time' in request_dict:
                licenses = licenses.filter(car_record_create_time__in=request_dict['car_record_create_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = CarSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


'''
@api_view(['GET','PUT','DELETE'])
def license_detail(request,pk,format=None):
    try:
        license = driving_license.objects.get(pk=pk)
    except driving_license.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrivingSerializer(license)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrivingSerializer(license,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        license.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#model_info查询
@api_view(['GET','POST'])
def model_info_list(request,format=None):
    #展示或者创建driving_license
    if request.method == 'GET':
        models_ = model_info.objects.all()
        serializer = ModelSerializer(models_,many=True)
        #print('get')
        #print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def model_info_detail(request,pk,format=None):
    try:
        models_ = model_info.objects.get(pk=pk)
    except model_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ModelSerializer(models_)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ModelSerializer(models_,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        models_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#user_info查询
@api_view(['GET','POST'])
def user_info_list(request,format=None):
    #展示或者创建driving_license
    if request.method == 'GET':
        users = user_info.objects.all()
        serializer = UserSerializer(users,many=True)
        #print('get')
        #print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def user_info_detail(request,pk,format=None):
    try:
        users = user_info.objects.get(pk=pk)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(users,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#登陆
@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':
        tel = request.POST.get('admin_tel','18855121479')
        pas = request.POST.get('admin_pas','wozhua')
        admin = admin_info.objects.filter(admin_tel__exact=tel,admin_pas__exact=pas)
        #filter返回QuerySet集合对象，遍历获得唯一元素
        if admin:
            for admin_item in admin:
                #print(admin_item)
                admin_serializer = AdminSerializer(admin_item)
            return Response(admin_serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'GET':
        admins = admin_info.objects.all()
        serializer = AdminSerializer(admins,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return  Response(status=status.HTTP_404_NOT_FOUND)

#管理员列表
class AdminList(generics.ListCreateAPIView):
    queryset = admin_info.objects.all()
    serializer_class = AdminSerializer

#管理详情
class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = admin_info.objects.all()
    serializer_class = AdminSerializer

#门店列表
class StoreList(generics.ListCreateAPIView):
    queryset = store_info.objects.all()
    serializer_class = StoreSerializer

    #def perform_create(self, serializer):
       # serializer.save(store_admin=self.request.)

#门店详情
class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = store_info.objects.all()
    serializer_class = StoreSerializer

#车辆列表
class CarList(generics.ListCreateAPIView):
    queryset = car_info.objects.all()
    serializer_class=CarSerializer

#车辆详情
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = car_info.objects.all()
    serializer_class=CarSerializer'''
