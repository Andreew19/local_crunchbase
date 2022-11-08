import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model

from startups.models import Startups, Categories, Articles, Founds

class CountableConnectionBase(graphene.relay.Connection):
  class Meta:
    abstract = True

  total_count = graphene.Int()

  def resolve_total_count(self, info, **kwargs):
    return self.iterable.count()

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

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
    me = graphene.Field(UserType)

    def resolve_categories(root, info):
      return Categories.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)