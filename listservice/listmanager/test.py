from django.test import TestCase
from .models import Todo, TodoList
from .serializers import TodoSerializer


class SerializersTests(TestCase):

    def test_todo_serializing_without_list(self):
        todo_message = "test todo"
        todo = Todo.objects.create(content=todo_message)
        ts = TodoSerializer(todo)
        self.assertEqual(ts.data, {"id": todo.id, "content": todo_message, "list": None})

    def test_todo_serializing_with_list(self):
        todo_message = "test todo"
        todo_list = TodoList.objects.create()
        todo = todo_list.todos.create(content=todo_message)
        ts = TodoSerializer(todo)
        self.assertEqual(ts.data, {"id": todo.id, "content": todo_message, "list": todo_list.id})

    def test_todo_deserializing_without_list(self):
        todo_message = "test todo"
        serialized_todo = {"content": todo_message, "list": None}
        ts = TodoSerializer(data=serialized_todo)
        ts.is_valid()
        new_todo = ts.save()
        self.assertEqual(new_todo.content, serialized_todo["content"])
        self.assertEqual(new_todo.list, serialized_todo["list"])

    def test_todo_deserializing_with_list(self):
        todo_message = "test todo"
        todo_list = TodoList.objects.create()
        serialized_todo = {"content": todo_message, "list": todo_list.id}
        ts = TodoSerializer(data=serialized_todo)
        ts.is_valid()
        new_todo = ts.save()
        self.assertEqual(new_todo.content, serialized_todo["content"])
        self.assertEqual(new_todo.list.id, serialized_todo["list"])
