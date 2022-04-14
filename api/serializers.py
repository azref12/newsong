from pyexpat import model
from rest_framework import serializers
from .models import *

class MyLaguSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Lagu
        fields = "__all__"
        
class MyRoomSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Room
        fields = "__all__"
        
class MySetupUrlSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Setupurl
        fields = "__all__"