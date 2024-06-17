from django.contrib import admin
from .models import Plan, Customer, Subscription


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'validity', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'email', 'number', 'registration_date', 'assigned_mobile_number')
    search_fields = ('name', 'email', 'phone_number')


admin.site.register(Subscription)
