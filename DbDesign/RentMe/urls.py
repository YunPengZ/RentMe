# coding:utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RentMe import views


urlpatterns = {
    url(r'^licenses/$',views.license_list),#驾驶证
    url(r'licenses/(?P<pk>[0-9]+)$',views.license_detail),
    #url(r'^model/$',views.ModelList.as_view(),name='model-list'),
    url(r'^model/$',views.model_info_list),#车型
    url(r'^model/(?P<pk>[0-9]+)$',views.model_info_detail),
    url(r'^car/$',views.CarList.as_view()),#车型
    url(r'^car/(?P<pk>[0-9]+)$',views.CarDetail.as_view()),
    url(r'^user/$',views.user_info_list),#用户
    url(r'^user/(?P<pk>[0-9]+)$',views.user_info_detail),
    url(r'^admins/$',views.AdminList.as_view()),#管理员
    url(r'^admins/(?P<pk>[0-9]+)$',views.AdminDetail.as_view(),name='admin-detail'),
    url(r'^stores/$',views.StoreList.as_view()),#门店
    url(r'^stores/(?P<pk>[0-9]+$)',views.StoreDetail.as_view()),
    url(r'^order/$',views.OrderList.as_view()),#租车订单
    url(r'^order/(?P<pk>[0-9]+$)',views.OrderDetail.as_view()),
    url(r'^relet/$',views.ReletList.as_view()),#续租记录
    url(r'^relet/(?P<pk>[0-9]+$)',views.ReletDetail.as_view()),

    #url(r'^cars/$',views.CarList.as_view()),#车辆
    #url(r'^cars/(?P<pk>[0-9]+)$',views.CarDetail.as_view()),
    url(r'^login/$',views.login),#登录
}


urlpatterns = format_suffix_patterns(urlpatterns)
