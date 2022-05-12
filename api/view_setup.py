from functools import partial
from inspect import isfunction
from tkinter import Y
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import AllowAny, IsAdminUser
import datetime
from rest_framework.decorators import api_view, permission_classes
from django.db import DatabaseError, transaction
from django.db.utils import IntegrityError

x = datetime.datetime.now()

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def setup_list (request):

        try:
                cek = request.GET['return_url']
                if cek == '/setup_list':
                        mastermodel = Setupurl
                        masterserialzer = MySetupUrlSerializer
                        serializerss = Setupurl1Serializer
                        serializer1 = Setupurl2Serializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)

        if request.method == 'GET':
                
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer (localmodel, many=True)
                localserializers = serializerss (localmodel, many=True)
                localserializer1 = serializer1 (localmodel, many=True)
        
                # fields = ('id')
                # localmodel = mastermodel.objects.all().only(fields)
                # localserializer = masterserialzer (localmodel, many=True)
                        
                # fields = ('rootpath')
                # localmodel = mastermodel.objects.all().only(fields)
                # localserializers = serializerss (localmodel, many=True)
                
                formater = {
                        # "master" : ({'id' : localserializer.data, 'rootpath' : localserializers.data})
                        "id" : localserializers.data,
                        "path" : localserializer1.data
                }
                                        
                return JsonResponse({'message' : 'successfully' , 'status' : True, 'count' : 1, 
                                     'results' : formater}, status=201)
        
        if request.method == 'POST':
                localrequest = JSONParser().parse(request)
                localserializer = masterserialzer(data=localrequest)
                with transaction.atomic():
                        sid = transaction.savepoint()
                        try:
                                if localserializer.is_valid():
                                        savesetup = Setupurl (
                                                                id = localrequest.data.get("id"),
                                                                rootpath = localrequest.data.get("rootpath"),
                                                                idbooth = localrequest.data.get("idbooth"),
                                                                ket = localrequest.data.get("ket")
                                                        )
                                        savesetup.save()
                                transaction.savepoint_commit(sid)
                        except IntegrityError:
                                transaction.savepoint_rollback(sid)

                        localmodel = mastermodel.objects.all()
                        localserializer = masterserialzer(localmodel, many=True)
                
                        formater = {
                                      "master" : localserializer.data
                        }
                                        
                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 
                                             'results' : formater}, status=201) 
        return JsonResponse(localserializer.errors, status=400)

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny]) 
def setup_detail (request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/setup_detail':
                        mastermodel = Setupurl
                        masterserialzer = MySetupUrlSerializer
                        serializerss = Setupurl1Serializer
                        serializer1 = Setupurl2Serializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)
        
        try:
                localmodel = mastermodel.objects.get(pk=pk)
        except mastermodel.DoesNotExist:
                return HttpResponse(status=404) 

        if request.method == 'GET':
        
                localserializer = masterserialzer(localmodel)
                return JsonResponse(localserializer.data)
    
        elif request.method == 'PUT': 
                localrequest = JSONParser().parse(request) 
                localserializer = masterserialzer(localmodel, data=localrequest) 

                if localserializer.is_valid(): 
                
                        localserializer.save()  
                
                        localmodel = mastermodel.objects.all()
                        localserializer = masterserialzer(localmodel, many=True)

                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                        status=201)
                return JsonResponse(localserializer.errors, status=400) 

        elif request.method == 'PATCH':
                localserializer = masterserialzer(localmodel, data={'status':0}, partial=True)
                if localserializer.is_valid():
                        localserializer.save()
                        return JsonResponse({'message': 'Success'}, status=200)
                else:
                        return JsonResponse(localserializer.errors, status=400)

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)        