from django.db import models
from django.utils.timezone import now

class Categories(models.Model):
  name = models.CharField(max_length=256, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

class Articles(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    link = models.CharField(max_length=256, blank=True, null=True)
    publicated_at = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)
    processed = models.BooleanField(default=False)
    article_categories = models.ManyToManyField(Categories)

class Startups(models.Model):
  name = models.CharField(max_length=256)
  description = models.CharField(max_length=1024)
  url = models.CharField(max_length=256, null=False)
  market = models.CharField(max_length=256, null=True)
  country = models.CharField(max_length=256, null=True)
  city = models.CharField(max_length=256, null=True)
  approoved = models.BooleanField(default=False)
  publicated_at = models.DateTimeField(default=now)
  updated_at = models.DateTimeField(default=now)

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

class Founds(models.Model):
  amount = models.IntegerField()
  startup = models.ForeignKey(Startups, on_delete=models.CASCADE)
  currency = models.CharField(max_length=3)
  approoved = models.BooleanField(default=False)
  publicated_at = models.DateTimeField(default=now)
