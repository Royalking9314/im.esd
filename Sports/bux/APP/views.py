from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import User

from .serializers import SportSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SportSerializer




