from functools import partial
from inspect import isfunction
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

x = datetime.datetime.now()

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def room_list (request):

    try:
        cek = request.GET['return_url']
        if cek == '/room_list':
            mastermodel = Room
            masterserialzer = MyRoomSerializer
            
    except cek.DoesNotExist:
        return HttpResponse(status=500)

    if request.method == 'GET':
        localmodel = mastermodel.objects.all()
        localserializer = masterserialzer(localmodel, many=True)
        return JsonResponse({'message': 'successfully', 'status': True, 'count': 1, 'results': localserializer.data})
    
    if request.method == 'POST':
        localrequest = JSONParser().parse(request)
        localserializer = masterserialzer(data=localrequest)

        if localserializer.is_valid():
            if cek == '/room_list':
                saveroom = Room (
                                    idroom = localrequest.data.get("idroom"),
                                    namaroom = localrequest.data.get("namaroom"),
                                    status = localrequest.data.get("status"),
                                    players = localrequest.data.get("players"),
                                    volmaster = localrequest.data.get("volmaster"),
                                    jam = localrequest.data.get("jam"),
                                    user = localrequest.data.get("user"),
                                    durasi = localrequest.data.get("durasi"),
                                    panggil = localrequest.data.get("panggil"),
                                    mac = localrequest.data.get("mac"),
                                    waktu = localrequest.data.get("waktu"),
                                    addtime = localrequest.data.get("addtime"),
                                    idandro = localrequest.data.get("idandro"),
                                    lastid = localrequest.data.get("lastid"),
                                    ip = localrequest.data.get("ip"),
                                    kondisi =localrequest.data.get("kondisi"),
                                    callopr =localrequest.data.get("callopr"),
                                    calltime = localrequest.data.get("calltime")
                            )
                saveroom.save()
            else:
                localserializer.save()

            localmodel = mastermodel.objects.all()
            localserializer = masterserialzer(localmodel, many=True)
            return JsonResponse({'message': 'successfully', 'status': True, 'count': 1, 'results': localserializer.data},
                                status=201)
        return JsonResponse(localserializer.errors, status=400)

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny]) 
def room_detail (request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/room_detail':
                        mastermodel = Room
                        masterserialzer = MyRoomSerializer
                
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