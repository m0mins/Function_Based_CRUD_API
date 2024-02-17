# serializers.py
from rest_framework import serializers
from function_crudApp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'description')
