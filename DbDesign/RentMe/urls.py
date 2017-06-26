# coding:utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RentMe import views


urlpatterns = {
    url(r'^licenses/$',views.license_list),
    url(r'licenses/(?P<pk>[0-9]+)$',views.license_detail),
    url(r'^login/$',views.login),
}


urlpatterns = format_suffix_patterns(urlpatterns)