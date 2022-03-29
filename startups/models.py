from django.db import models
# Create your models here.
#for test



class Categories(models.Model):
  name = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField
    link = models.CharField(max_length=256, blank=True, null=True)
    publicated_at = models.DateTimeField('date published')
    creator = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)
    article_categories = models.ManyToManyField(Categories)

class Startups(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField
  url = models.TextField(null=False)
  market = models.TextField
  country = models.TextField
  city = models.TextField
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')

class TagGroups(models.Model):
  name = models.CharField(max_length=256)
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')

class Tags(models.Model):
  name = models.CharField(max_length=256)
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')
  tag_group_id = models.BigAutoField(primary_key=True)
  startups_tags = models.ManyToManyField(TagGroups)


