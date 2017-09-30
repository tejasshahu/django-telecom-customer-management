Some Basic Commands for Using Django in Windows 7

cd 'directory name' : change directory
mkdir 'directory name' : make directory
install virtualenv and virtualwrapper : pip install virtualenvwrapper-win (https://docs.djangoproject.com/en/1.10/howto/windows/)
first install virtual environment: pip install virtualenv
Create Virtual Enviroment : virtualenv 'name of environment' (http://docs.python-guide.org/en/latest/dev/virtualenvs/)
Activate Virtual Mode : 'Virtual env name'\Scripts\activate
Deactivate Virtual Mode : deactivate
Installing Django: pip install django~=1.7.2 ('~' means it will install nearly version and '==' for exactly that)
Check Django Version:  First activate virtual environment and type command "pip show django" (it will show installed django version)

Step(1)
Start new project: before create one folder for project then write below command
django-admin startproject crud_app2 .(don't forgect to add this "." stands for)

step(2)
Start new app:
python manage.py startapp company

step(3)
Run initial migration:
python manage.py migrate

step(4)
create a superuser:
python manage.py createsuperuser
username-
pass-

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
execute migrations-apply those changes to the database
python manage.py migrate

note: after making any changes in models run step 7 and 8


Git commands

(1)To check new changes
git status

(2)To add all files for commit
git add *

(3)To commit a added code 
git commit -m "commit msg"

(4)Push the code to github.com
git push
