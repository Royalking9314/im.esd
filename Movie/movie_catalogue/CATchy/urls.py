
from django.urls import path, include
from . import views
from . views import MovieViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'Movie', viewset=views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
