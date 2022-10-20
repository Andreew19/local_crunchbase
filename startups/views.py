from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,ArticleSerializer,StartupsSerializing,TagGroupsSerializing,TagsSerializing
from .models import Categories, Articles, Startups, TagGroups, Tags
from rest_framework.response import Response

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategorySerializer

class ArticlesViewSet(viewsets.ModelViewSet):
  queryset = Articles.objects.all()
  serializer_class = ArticleSerializer

  def create(self,request, *args, **kwargs):
    data = request.data

    new_article = Articles.objects.create(
      title = data["title"],
      link = data["link"],
      publicated_at = data["publicated_at"]
    )

    new_article.save()

    for category in data['article_categories']:
        category_obj = Categories.objects.get(name = category)
        new_article.article_categories.add(category_obj)

    serializer = ArticleSerializer(new_article)

    print(serializer.data)

    return Response(serializer.data)

class StartupsViewSet(viewsets.ModelViewSet):
  queryset = Startups.objects.all()
  serializer_class = StartupsSerializing

class TagGroupsViewSet(viewsets.ModelViewSet):
  queryset = TagGroups.objects.all()
  serializer_class = TagGroupsSerializing

class TagsViewSet(viewsets.ModelViewSet):
  queryset = Tags.objects.all()
  serializer_class = TagsSerializing