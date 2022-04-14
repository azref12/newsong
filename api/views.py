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
from .serializers import MyLaguSerializer
from django.db import DatabaseError, transaction
from django.db.utils import IntegrityError

x = datetime.datetime.now()

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def Generals_list (request):

    try:
        cek = request.GET['return_url']
        if cek == '/lagu_list':
            mastermodel = Lagu
            masterserialzer = MyLaguSerializer
        if cek == '/room_list':
            mastermodel = Room
            masterserialzer = MyRoomSerializer
        if cek == '/setupurl_list':
            mastermodel = Setupurl
            masterserialzer = MySetupUrlSerializer
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
                try:
                        res = Lagu.objects.filter(idlagu = y)
                        x = int (res.idlagu[0:500])
                        print(x)
                except :
                        x=1
                                
                y = x
                with transaction.atomic():
                        sid = transaction.savepoint()
                        try:
                                if localserializer.is_valid():
                                        savelagu = Lagu (
                                                        idlagu = localrequest.data.get("idlagu"),
                                                        edp = localrequest.data.get("edp"),
                                                        dup = localrequest.data.get("dup"),
                                                        judul = localrequest.data.get("judul"),
                                                        artis = localrequest.data.get("artis"),
                                                        path = localrequest.data.get("path"),
                                                        cont = localrequest.data.get("cont"),
                                                        dur = localrequest.data.get("dur"),
                                                        size = localrequest.data.get("size"),
                                                        voc = localrequest.data.get("voc"),
                                                        xvoc = localrequest.data.get("xvoc"),
                                                        gol = localrequest.data.get("gol"),
                                                        jenis = localrequest.data.get("jenis"),
                                                        vol = localrequest.data.get("vol"),
                                                        vol2 = localrequest.data.get("vol2"),
                                                        vol3 = localrequest.data.get("vol3"),
                                                        rms = localrequest.data.get("rms"),
                                                        rms2 = localrequest.data.get("rms2"),
                                                        rms3 = localrequest.data.get("rms3"),
                                                        hits = localrequest.data.get("hits"),
                                                        new = localrequest.data.get("new"),
                                                        popular = localrequest.data.get("popular"),
                                                        idsource = localrequest.data.get("idsource"),
                                                        datetime = localrequest.data.get("datetime"),
                                                        hade = localrequest.data.get("hade"),
                                                        judul2 = localrequest.data.get("judul2"),
                                                        judul3 = localrequest.data.get("judul3"),
                                                        exjudul = localrequest.data.get("exjudul"),
                                                        artis2 = localrequest.data.get("artis2"),
                                                        artis3 = localrequest.data.get("artis3"),
                                                        exartis = localrequest.data.get("exartis"),
                                                        rev = localrequest.data.get("rev"),
                                                        keterangan = localrequest.data.get("keterangan"),
                                                        masalah = localrequest.data.get("masalah"),
                                                        drive = localrequest.data.get("drive"),
                                                        status = localrequest.data.get("status"),
                                                        posisi = localrequest.data.get("posisi")
                                                )
                                        savelagu.save()
                                transaction.savepoint_commit(sid)
                        except IntegrityError:
                                transaction.savepoint_rollback(sid)

                                ModelMaster = Lagu.objects.filter(y)
                                MasterSerializer = MyLaguSerializer (ModelMaster, many=True)
                                
                                formater = {
                                        "master": MasterSerializer.data

                                }
                            
                                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                    status=201)  
@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny]) 
def general_detail (request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/lagu_detail':
                        mastermodel = Lagu
                        masterserialzer = MyLaguSerializer
                
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