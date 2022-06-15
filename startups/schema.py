import graphene
from graphene_django import DjangoObjectType

from startups.models import Startups, Categories, Articles

class StartupType(DjangoObjectType):
  class Meta:
    model = Startups
    fields = ("id", "name")

class CategoryType(DjangoObjectType):
  class Meta:
    model = Categories
    fields = ("id", "name")

class ArticleType(DjangoObjectType):
  class Meta:
    model = Articles
    fields = ("title", "description", "link", "processed")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    startups = graphene.List(StartupType)
    categories = graphene.List(CategoryType)
    articles = graphene.List(ArticleType)

    def resolve_startups(root, info):
      return Startups.objects.all()

    def resolve_categories(root, info):
      return Categories.objects.all()

    def resolve_articles(root, info):
      return Articles.objects.all()

schema = graphene.Schema(query=Query)