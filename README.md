# django-lab
Testing Django

Steps to get started

* Install the latest python3
* Set up virtual environment for project folder
* Install Django
* Set up Visual Studio Code to handle python and venv
* Create a Django project
* Create a Django app insida the project
* Add Django rest framework to project 

## Teminology
A Django project is a collection of configuration and apps for a particular website

An app is a Web application the projectfolder that does something (blog, todolist, api, users)

## Reference
https://docs.djangoproject.com/en/3.0/intro/tutorial01/

## Initial step
```
django-admin startproject todoproject
```

set venv

```
python3 -m venv venv
```

Activate the venv in current shell/session
```
source venv/bin/activate
```

Set Visual Studio python interpreter

CMD + SHIFT + P

Python: Selecter interpreter
```
./venv/bin/python
```

By default, VS Code uses the interpreter identified by python:pythonPath setting when debugging code.

Set python.pythonPath setting

CMD + ,   (setttings)
```
${workspaceFolder}/venv/bin/python
```

Enable automatic py env activation
CMD + ,    (settings)
then search for 'python.terminal.activate'
Enable both settings
* active env in current terminal
* activate environment
```
python.terminal.activateEnvironment : true
```

install dependencies (if any)
```
pip install -r requirements.txt
```

install Django
```
pip install Django
```

Initialize database
```
python todoproject/manage.py migrate
```
A project db.sqlite3 is created and populated with default tables

Testing the server
```
python todoproject/manage.py runserver
```

Adding a todo-app to the todosystem
```
python todoproject/manage.py startapp todoapp
```

Added a new view 
edit todoapp/views.py to add the new view
A simple test
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Add URL config

```
touch todoapp/urls.py
```
Add url config for the todo app
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

```
touch todoapp/urls.py
```

```
python todoproject/manage.py createsuperuser
```

## Django REST framework
https://www.django-rest-framework.org/