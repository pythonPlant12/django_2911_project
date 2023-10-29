from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from authors import views

router = DefaultRouter()


router.register(r"authors", views.AuthorsViewSet, basename='Authors')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("authors/", include("authors.urls")),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path("__debug__/", include("debug_toolbar.urls"))
]
    # path("books/", include("books.urls")),
