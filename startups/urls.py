from django.urls import include, path
from rest_framework import routers
from .views import CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoriesViewSet)

urlpatterns = [
  path('', include(router.urls)),
]