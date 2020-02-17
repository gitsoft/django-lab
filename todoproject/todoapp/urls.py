from django.urls import path

from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    # ex: http://localhost:8000/todoapp/1/
    path('<int:todolist_id>/', views.todolist, name='todolist'),
    # ex: http://localhost:8000/todoapp/1/details/
    path('<int:todo_id>/details/', views.tododetails, name='results'),
]

