from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^employee_list', views.employee_list, name='employee_list'),
 	url(r'^employee_create', views.employee_create, name='employee_create'),
 	url(r'^employee_update/(?P<pk>\d+)$', views.employee_update, name='employee_update'),
 	url(r'^employee_delete/(?P<pk>\d+)$', views.employee_delete, name='employee_delete'),
 	url(r'^script', views.employee_create, name='employee_create'),
]