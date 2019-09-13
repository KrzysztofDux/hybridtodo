from collections import OrderedDict

from django.test import TestCase

from .models import Todo, TodoList
from .serializers import TodoSerializer, TodoListSerializer


class TodoSerializersTests(TestCase):
    todo_message = "test todo"

    def test_todo_serialization_without_list(self):
        todo = Todo.objects.create(content=self.todo_message)
        ts = TodoSerializer(todo)
        self.assertDictEqual(ts.data, self.get_expected_serialized_todo(todo))

    def test_todo_serialization_with_list(self):
        todo_list = TodoList.objects.create()
        todo = todo_list.todos.create(content=self.todo_message)
        ts = TodoSerializer(todo)
        self.assertDictEqual(ts.data, self.get_expected_serialized_todo(todo, todo_list.id))
        self.assertIn(todo, todo_list)

    def get_expected_serialized_todo(self, todo, todo_list_id=None):
        return {'id': todo.id, 'content': self.todo_message, 'list': todo_list_id}

    def test_todo_deserialization_without_list(self):
        json_todo = {"content": self.todo_message, "list": None}
        ts = TodoSerializer(data=json_todo)
        ts.is_valid()
        new_todo = ts.save()
        self.assertEqual(new_todo.content, json_todo["content"])
        self.assertEqual(new_todo.list, json_todo["list"])

    def test_todo_deserialization_with_list(self):
        todo_list = TodoList.objects.create()
        json_todo = {"content": self.todo_message, "list": todo_list.id}
        ts = TodoSerializer(data=json_todo)
        ts.is_valid()
        new_todo = ts.save()
        self.assertEqual(new_todo.content, json_todo["content"])
        self.assertEqual(new_todo.list.id, json_todo["list"])
        self.assertIn(new_todo, todo_list)


class TodoListSerializersTests(TestCase):

    def test_todo_list_serialization(self):
        todo_message = "test todo"
        todo_list = TodoList.objects.create()
        td1 = todo_list.todos.create(content=todo_message)
        td2 = todo_list.todos.create(content=f"{todo_message} 2")
        tls = TodoListSerializer(todo_list)
        expected = {"id": todo_list.id, "todos": [self.get_todo(td1), self.get_todo(td2)]}
        self.assertDictEqual(tls.data, expected)

    def get_todo(self, todo):
        return OrderedDict([("id", todo.id), ("content", todo.content)])
