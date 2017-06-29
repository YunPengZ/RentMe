# coding:utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RentMe import views


#关于URL使用说明
#如果添加了正在使用的url请放在正在使用区


urlpatterns = {
    #>>>>>>>>>>>>>>>>正在使用的url
    url(r'^model/$',views.model_list),
    url(r'^licenses/$',views.license_list),#驾驶证

    url(r'^car/$',views.car_list),#车辆
    url(r'^car/$',views.car_list),
    url(r'^user/$',views.user_list),#用户
    #url(r'^admins/$',views.AdminList.as_view()),#管理员
    url(r'^admins/$',views.admin_list),#管理员
    url(r'^stores/$',views.store_list),#门店
    url(r'^relet/$',views.relet_list),#续租记录
    url(r'^illegal/$',views.illegal_list),
    url(r'^login/$',views.login),#登录

    url(r'^order/$',views.OrderList.as_view()),#租车订单
    #url(r'^order/$',views.OrderList.as_view()),
    url(r'^order/type$',views.get_car_info_by_type),
    url(r'^order/date$',views.get_car_info_by_date),
    url(r'^order/pay$',views.OrderList.as_view()),
    url(r'^order/date_type$',views.get_car_info_by_dateAndStore),


    #>>>>>>>>>>>>>>>未使用的url
    #modify 临时修改数据库时建立的接口
    #url(r'^modify/$',views.modify),
    url(r'licenses/(?P<pk>[0-9]+)$',views.license_detail),
    #url(r'^model/$',views.ModelList.as_view(),name='model-list'),
    url(r'^model/(?P<pk>[0-9]+)$',views.model_info_detail),
    #url(r'^cars/$',views.CarList.as_view()),#车辆
    url(r'^car/(?P<pk>[0-9]+)$',views.CarDetail.as_view()),
    #url(r'^car/(?P<pk>[0-9]+)$',views.CarDetail.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$',views.user_info_detail),
    url(r'^admins/(?P<pk>[0-9]+)$',views.AdminDetail.as_view(),name='admin-detail'),
    url(r'^order/(?P<pk>[0-9]+$)',views.OrderDetail.as_view()),
    url(r'^stores/(?P<pk>[0-9]+$)',views.StoreDetail.as_view()),
    url(r'^relet/(?P<pk>[0-9]+$)',views.ReletDetail.as_view()),
    url(r'^illegal/(?P<pk>[0-9]+$)',views.IllegalDetail.as_view()),
}


urlpatterns = format_suffix_patterns(urlpatterns)
