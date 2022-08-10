from django.db import models
# Create your models here.



class Categories(models.Model):
  name = models.CharField(max_length=256, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
      #Исправляет баг с "s" по умолчанию в конце слова
      verbose_name_plural = 'Categories'

  def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField
    link = models.CharField(max_length=256, blank=True, null=True)
    publicated_at = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)
    processed = models.BooleanField(default=False)
    article_categories = models.ManyToManyField(Categories)
    class Meta:
      #Исправляет баг с "s" по умолчанию в конце слова
      verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

class Startups(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField
  url = models.TextField(null=False)
  market = models.TextField
  country = models.TextField
  city = models.TextField
  approoved = models.BooleanField(default=False)
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')
  class Meta:
    #Исправляет баг с "s" по умолчанию в конце слова
    verbose_name_plural = 'Startups'

class TagGroups(models.Model):
  name = models.CharField(max_length=256)
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')
  class Meta:
    #Исправляет баг с "s" по умолчанию в конце слова
    verbose_name_plural = 'Tags group'

class Tags(models.Model):
  name = models.CharField(max_length=256)
  publicated_at = models.DateTimeField('date published')
  updated_at = models.DateTimeField('date updated')
  tag_group_id = models.BigAutoField(primary_key=True)
  startups_tags = models.ManyToManyField(TagGroups)
  class Meta:
    #Исправляет баг с "s" по умолчанию в конце слова
    verbose_name_plural = 'Tags'

class Founds(models.Model):
  amount = models.IntegerField()
  startup = models.ForeignKey(Startups, on_delete=models.CASCADE)
  currency = models.CharField(max_length=3)
  approoved = models.BooleanField(default=False)
  publicated_at = models.DateTimeField('date published')
