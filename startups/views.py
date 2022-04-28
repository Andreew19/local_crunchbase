from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriesSerializing,ArticlesSerializing,StartupsSerializing,TagGroupsSerializing,TagsSerializing
from .models import Categories, Articles, Startups, TagGroups, Tags
# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategoriesSerializing


class ArticlesViewSet(viewsets.ModelViewSet):
  queryset = Articles.objects.all()
  serializer_class = ArticlesSerializing

class StartupsViewSet(viewsets.ModelViewSet):
  queryset = Startups.objects.all()
  serializer_class = StartupsSerializing

class TagGroupsViewSet(viewsets.ModelViewSet):
  queryset = TagGroups.objects.all()
  serializer_class = TagGroupsSerializing

class TagsViewSet(viewsets.ModelViewSet):
  queryset = Tags.objects.all()
  serializer_class = TagsSerializing

