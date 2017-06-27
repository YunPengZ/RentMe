# coding:utf-8
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RentMe import models
from RentMe.serializers import *

@api_view(['GET','POST'])
def license_list(request,format=None):
    #展示或者创建driving_license
    if request.method == 'GET':
        licenses = driving_license.objects.all()
        serializer = DrivingSerializer(licenses,many=True)
        print('get')
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('post')
            print(Response(serializer.data))
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

