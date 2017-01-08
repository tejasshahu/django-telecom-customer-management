from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^employee_list', views.employee_list, name='employee_list'),
]