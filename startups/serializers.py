from rest_framework import serializers
from .models import Categories

class CategoriesSerializing(serializers.ModelSerializer):
    class Meta: 
      model = Categories
      fields = ('name',)