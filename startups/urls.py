from django.urls import include, path
from rest_framework import routers
from .views import CategoriesViewSet, ArticlesViewSet,StartupsViewSet,TagGroupsViewSet,TagsViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'startups', StartupsViewSet)
router.register(r'tags_groups', TagGroupsViewSet)
router.register(r'tags', TagsViewSet)

urlpatterns = [
  path('', include(router.urls)),
]