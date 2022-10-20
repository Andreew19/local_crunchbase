import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from startups.models import Startups, Categories, Articles, Founds

class CountableConnectionBase(graphene.relay.Connection):
  class Meta:
    abstract = True

  total_count = graphene.Int()

  def resolve_total_count(self, info, **kwargs):
    return self.iterable.count()

class FoundType(DjangoObjectType):
  class Meta:
    model = Founds
    fields = ("id", "amount", "currency", "publicated_at")

class StartupType(DjangoObjectType):
  class Meta:
    model = Startups
    fields = ("id", "name", "url", "description")
    interfaces = (graphene.relay.Node,)
    filter_fields = {
      'name': ['exact']
    }
    connection_class = CountableConnectionBase

  founds = graphene.List(FoundType)

  def resolve_founds(self, info):
    return self.founds_set.all()

class CategoryType(DjangoObjectType):
  class Meta:
    model = Categories
    fields = ("id", "name")

  article_count = graphene.Int()

  def resolve_article_count(root, info):
    return 12

class ArticleNode(DjangoObjectType):
  class Meta:
    model = Articles
    fields = ("id", "title", "link", "processed", "article_categories")
    interfaces = (graphene.relay.Node,)
    filter_fields = {
      'title': ['exact']
    }
    connection_class = CountableConnectionBase

class Query(graphene.ObjectType):
    startups = DjangoFilterConnectionField(StartupType)
    categories = graphene.List(CategoryType)
    articles = DjangoFilterConnectionField(ArticleNode)

    def resolve_categories(root, info):
      return Categories.objects.all()

schema = graphene.Schema(query=Query)