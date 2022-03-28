from django.db import models
# Create your models here.



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



