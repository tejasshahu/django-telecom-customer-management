from django.db import models

# Create your models here.

class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	designation = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.first_name 

#	class Detail(models.Model):
#	Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

