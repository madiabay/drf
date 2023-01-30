from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Women, Category
from .serializers import WomenSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomenAPIList(generics.ListCreateAPIView):

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)