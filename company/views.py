from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from company.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'designation']

def index(request):
	return HttpResponse("<h1>This is the company app home page<h1>")

def employee_list(request, template_name='company_template/employee_list.html'):
    employee = Employee.objects.all()
    data = {}
    data['object_list'] = employee
    return render(request, template_name, data)


def employee_create(request, template_name='company_template/employee_form.html'):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/company/employee_list.html')
    return render(request, template_name, {'form':form})