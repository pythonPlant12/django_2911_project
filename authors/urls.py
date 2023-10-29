from django.urls import include, path
from rest_framework import routers

from authors.views import AuthorsViewSet

router = routers.SimpleRouter()
router.register(r'', AuthorsViewSet, basename='Authors')

urlpatterns  = []