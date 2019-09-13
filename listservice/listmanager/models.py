from django.db import models


class TodoList(models.Model):
    id = models.AutoField(primary_key=True)


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    list = models.ForeignKey(TodoList, related_name="todos", null=True, on_delete=models.SET_NULL)
