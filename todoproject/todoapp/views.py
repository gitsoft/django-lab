from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Todo

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def defaultlist(request):
    latest_todos = Todo.objects.order_by('-created_date')[:20]
    output = ', '.join([todo.short_text for todo in latest_todos])
    return HttpResponse(output)

def todolist(request, todolist_id):
    response = "You're looking at the todo list with id %s."
    return HttpResponse(response % todolist_id)

def tododetails(request, todo_id):
    return HttpResponse("You're looking at todo %s." % todo_id)

