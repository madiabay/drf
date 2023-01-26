from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': lst})
    
    def post(self, request):
        post_new = Women.objects.create(**request.data)
        return Response({'post': model_to_dict(post_new)})

# class WomenAPIView(generics.ListAPIView):

#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer