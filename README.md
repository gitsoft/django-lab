# django-lab
Testing Django

## Reference
https://docs.djangoproject.com/en/3.0/intro/tutorial01/

## Initial step
```
django-admin startproject todo
```

set venv

```
python3 -m venv venv
```

install dependencies (if any)
```
pip install -r requirements.txt
```

Initialize database
```
python manage.py migrate
```

Testing the server
```
python manage.py runserver
```

Adding a todo-app to the todosystem
```
python manage.py startapp todoapp
```
