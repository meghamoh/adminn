from django.shortcuts import render

from rest_framework import viewsets
from adminn.models import User
from adminn.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]