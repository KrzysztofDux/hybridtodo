from rest_framework import serializers
from .models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'content', 'list')

class TodoSerializerForList(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'content')

class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializerForList(many=True, required=False)

    class Meta:
        model = TodoList
        fields = ('id', 'todos')
