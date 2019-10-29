from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name = 'work'),
    path('addTodo/', views.addTodo, name = 'work'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name = 'work'),
]