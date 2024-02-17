from function_crudApp import views
from django.urls import path

urlpatterns = [
    path('todos/', views.getStudents),
    path('todo/<int:pk>/', views.getStudent),
    path('create/', views.createfunc),
    path('update/<int:pk>/', views.update_todo),
    path('delete/<int:pk>/', views.delete_todo),
]
