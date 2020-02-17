from django.core import serializers
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Todo

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def defaultlist(request):
    latest_todos = Todo.objects.order_by('-created_date')[:20]
    # output = ', '.join([todo.short_text for todo in latest_todos])
    # return HttpResponse(output)
    template = loader.get_template('defaultlist.html') 
    context = {
        'latest_todos': latest_todos,
    }
    return HttpResponse(template.render(context, request))    

def todolist(request, todolist_id):
    response = "You're looking at the todo list with id %s."
    return HttpResponse(response % todolist_id)

def tododetails(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    # output = str(todo.short_text) + ' <br>' + str(todo.long_text) + ' <br>' + str(todo.completed) + ' <br>' + str(todo.created_date) 
    output = serializers.serialize("json", [todo])
    return HttpResponse(output)

    # return HttpResponse("You're looking at todo %s." % todo_id)

