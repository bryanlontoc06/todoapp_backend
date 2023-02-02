from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo_api import views

router = DefaultRouter()
router.register('todo', views.TodoItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
