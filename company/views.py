from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from company.models import Employee

def index(request):
	return HttpResponse("<h1>This is the company app home page<h1>")

def employee_list(request, template_name='company_template/employee_list.html'):
    employee = Employee.objects.all()
    data = {}
    data['object_list'] = employee
    return render(request, template_name, data)