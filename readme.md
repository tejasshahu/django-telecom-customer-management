Step(1)
start new project:
django-admin startproject crud_app2 .

step(2)
Start new app:
python manage.py startapp company

step(3)
run initial migration
python manage.py migrate

step(4)
create a superuser
python manage.py createsuperuser
username-admin
pass-admin

step(5)
add app to settings.py under in installed app
'name of app'

step(6)
create new model in company app's model.py file

class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30) 

step(7)
generate migrations file to update database
python manage.py makemigrations

step(8)
execute migrations 
python manage.py migrate

note: after making any changes in models run step 7 and 8