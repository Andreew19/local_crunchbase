from rest_framework import serializers
from .models import Categories, Articles, Startups, TagGroups, Tags

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
      model = Categories
      fields = ('name', 'id')

class ArticleSerializer(serializers.ModelSerializer):
  article_categories = CategorySerializer(read_only=True, many=True)

  class Meta:
    model = Articles
    fields = ('id', 'title', 'article_categories', 'link', 'publicated_at')

class StartupsSerializing(serializers.ModelSerializer):
    class Meta:
      model = Startups
      fields = ('name', 'description', 'url', 'market', 'country', 'city', 'publicated_at', 'updated_at',)

class TagGroupsSerializing(serializers.ModelSerializer):
  class Meta:
    model = TagGroups
    fields = ('name', 'publicated_at', 'updated_at',)

class TagsSerializing(serializers.ModelSerializer):
  class Meta:
    model = Tags
    fields = ('name', 'publicated_at', 'updated_at', 'tag_group_id', 'startups_tags',)
