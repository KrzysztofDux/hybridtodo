from django.db import models


class TodoList(models.Model):
    id = models.AutoField(primary_key=True)

    def __getitem__(self, item):
        return list(self.todos.all())[item]


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    list = models.ForeignKey(TodoList, related_name="todos", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content
