from django.urls import include
from rest_framework import routers
from .views import UserViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register(r'User', UserViewSet)

urlpatterns = [
    path('user/', include(router.urls)),

]