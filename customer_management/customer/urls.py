from django.urls import path

from .views import (ChoosePlanView, \
                    CustomerListView,
                    CustomerDetailView, RegisterCustomerView)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<int:customer_id>/choose_plan/', ChoosePlanView.as_view(), name='choose_plan'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('register/', RegisterCustomerView.as_view(), name='register_customer'),
]
