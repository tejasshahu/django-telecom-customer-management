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
        keys1 = []
        values1 = []

        import pdb
        pdb.set_trace()

        keys1 = map(str,request.POST.dict().keys())
        values1 = map(str,request.POST.dict().values())

        keys2 = keys1[1:]
        values2 = values1[1:]

        data_dictionary = dict(zip(keys2, values2))

        context = data_dictionary

        print context

        # return redirect(request,'script.html',context)

        return redirect('/company/employee_list.html')
    return render(request, template_name, {'form':form})

def employee_update(request, pk, template_name='company_template/employee_form.html'):
    employee= get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():

        form.save()

        return redirect('/company/employee_list.html')
    return render(request, template_name, {'form':form})

def employee_delete(request, pk, template_name='company_template/employee_confirm_delete.html'):
    employee= get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('/company/employee_list.html')
    return render(request, template_name, {'object':employee})