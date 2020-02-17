from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Todolist(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created')

class Todo(models.Model):
    short_text = models.CharField(max_length=100)
    long_text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField('date created')
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)

