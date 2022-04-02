from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriesSerializing
from .models import Categories
# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategoriesSerializing