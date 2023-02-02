from rest_framework import serializers
from todo_api import models


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoItem
        fields = ('id', 'text', 'isCompleted', 'created_on')