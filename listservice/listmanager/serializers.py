from rest_framework import serializers
from .models import Todo, TodoList


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id')


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'content', 'list')
