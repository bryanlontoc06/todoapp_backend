from rest_framework import viewsets

from todo_api import serializers
from todo_api import models

# Create your views here.


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoItemSerializer
    queryset = models.TodoItem.objects.all()