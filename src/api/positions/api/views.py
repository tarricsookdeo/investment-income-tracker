from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from positions.models import Position

from .serializers import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """ Viewset to CRUD Position objects """
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
