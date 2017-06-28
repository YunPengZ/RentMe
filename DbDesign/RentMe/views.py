# coding:utf-8
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from RentMe.models import *
from RentMe.serializers import *
import json
import datetime
#license_info查询
@api_view(['GET','POST'])
def license_list(request,format=None):
    #展示或者创建driving_license
    if request.method == 'GET':
        licenses = driving_license.objects.all()
        serializer = DrivingSerializer(licenses,many=True)
        #print('get')
        #print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET','POST'])
def get_car_info_by_type(request):
    dict_type = dict()
    json_dict = dict()
    dict_type['商务车'] = 0
    dict_type['SUV'] = 0
    dict_list = list()
    for order in rent_order.objects.all():
        car = order.car_num
        model = car.car_model_id
        if(model.car_type == 0):
            dict_type['商务车'] +=1
        elif (model.car_type == 1):
            dict_type['SUV'] +=1
    for key,values in dict_type.items():
        #json_dict['car_type'] = key
        #json_dict['car_count'] = values
        dict_list.append({'car_type':key,'car_count':values})
        print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def get_car_info_by_date(request):
    query_dict = dict()
    dict_list = list()
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month):
        query_dict[order.pick_time.date().isoformat()] = 0
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month): 
        query_dict[order.pick_time.date().isoformat()] = query_dict[order.pick_time.date().isoformat()] + 1
    for key,values in query_dict.items():
        dict_list.append({'pick_time':key,'car_count':values})
        print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def get_car_info_by_dateAndStore(request):
    query_dict = dict()
    dict_list = list()
    result_dict = dict()
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month):
            query_dict[order.pick_time.date().isoformat()] = dict()
    for store in store_info.objects.all():
        for order in store.pick_store.filter(pick_time__month=datetime.datetime.now().month):
            query_dict[order.pick_time.date().isoformat()]['store_count'+str(store.store_id)] = 0
    for store in store_info.objects.all():
        for order in store.pick_store.filter(pick_time__month=datetime.datetime.now().month):
            print(order.pick_addr)
            query_dict[order.pick_time.date().isoformat()]['store_count'+str(store.store_id)] += 1 
    for key,values in query_dict.items():
        dict_list.append({"pick_time":key,"store_count":values})
    print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def order_pay(request):
    json_query = dict()
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            order = rent_order.objects.get(pk=serializer.data['order_id'])
            json_query['form'] = dict()
            json_query['form']['pick_add'] = order.pick_addr.store_addr
            json_query['form']['pick_time'] = order.pick_time
            json_query['form']['drop_time'] = order.drop_time
            json_query['user_deposit'] = order.actual_deposit
            json_query['car_deposit'] = order.car_num.car_model_id.car_deposit
            json_query['user_name'] = order.user_num.user_name
            json_query['drive_name'] = order.user_drive.drive_name
            json_query['car_num'] = order.car_num.car_num
            json_query['car_brand'] = order.car_num.car_model_id.car_brand
            json_query['car_series'] = order.car_num.car_model_id.car_series
            json_query['car_config_model'] = order.car_num.car_model_id.car_config_model
            
            return Response(json_query,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)  

class ModelList(generics.ListCreateAPIView):
    queryset = model_info.objects.all()
    serializer_class = ModelSerializer

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
   # def perform_create(self, serializer):
       # print(self.request.POST)
       ## model_at = model_info.objects.get(pk=self.request.POST.car_model_id)
       # serializer.save(model_at)

#车辆详情
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = car_info.objects.all()
    serializer_class=CarSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = rent_order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rent_order.objects.all()
    serializer_class = OrderSerializer

class ReletList(generics.ListCreateAPIView):
    queryset = relet_record.objects.all()
    serializer_class = ReletSerializer

class ReletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = relet_record.objects.all()
    serializer_class = ReletSerializer