from rest_framework import serializers
from .models import Categories, Articles, Startups, TagGroups, Tags

class CategoriesSerializing(serializers.ModelSerializer):
    class Meta: 
      model = Categories
      fields = ('name',)

class ArticlesSerializing(serializers.ModelSerializer):
  class Meta:
    model = Articles
    fields = ('title', 'description', 'link', 'publicated_at', 'creator', 'type', 'article_categories',)

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
