from django.urls import path, include
from .views import  UserViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('User/', include(router.urls)),
   
]
