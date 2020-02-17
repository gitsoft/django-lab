from django.urls import path

from . import views

urlpatterns = [
    # ex: http://localhost:8000/todoapp/
    path('', views.defaultlist, name='todolist'),
    # ex: http://localhost:8000/todoapp/1/
    path('<int:todolist_id>/', views.todolist, name='todolist'),
    # ex: http://localhost:8000/todoapp/1/details/
    path('<int:todo_id>/details/', views.tododetails, name='results'),
]

