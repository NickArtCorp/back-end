from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class ModelSerializer:
      model = Menu
      fields = '__all__'