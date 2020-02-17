from django.contrib import admin
from .models import Todolist
from .models import Todo
# Register your models here.

admin.site.register(Todo)
admin.site.register(Todolist)