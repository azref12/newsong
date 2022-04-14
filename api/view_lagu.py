from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import MyLaguSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# import datetime
from rest_framework import generics

if __name__ == "__main__": 
    print(Lagu.objects.all())
    
class LaguList (generics.ListCreateAPIView) :
        queryset = Lagu.objects.all()
        serializer_class = MyLaguSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['idlagu'] 
        ordering_fields = ['judul','artis','judul2','judul3','exjudul','artis2','artis3','exartis']
        search_fields = ['judul','artis','judul2','judul3','exjudul','artis2','artis3','exartis'] 
        
class LaguDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = Lagu.objects.all() 
        serializer_class = MyLaguSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['idlagu']  
        ordering_fields = ['judul','artis','judul2','judul3','exjudul','artis2','artis3','exartis']
        search_fields = ['judul','artis','judul2','judul3','exjudul','artis2','artis3','exartis']

