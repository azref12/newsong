from rest_framework import routers
from django.urls import path, include
from api import views
from api import view_room
from api import view_setup
from api import view_lagu
from .views import *
from .customejwt import LogoutView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path ('', include(router.urls)),
    path ('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path ('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path ('logout/', LogoutView.as_view(), name='auth_logout'),
    path ('api/generals/', views.Generals_list, name='Generals_list'),
    path ('api/general_detail/<int:pk>/', views.general_detail, name='general_detail'),
    path ('api/', view_lagu.LaguList.as_view(queryset=Lagu.objects.all(), 
                                    serializer_class=MyLaguSerializer), name='LaguList'),
    path ('api/', view_lagu.LaguDetail.as_view(queryset=Lagu.objects.all(), 
                                    serializer_class=MyLaguSerializer), name='LaguDetail'),
    path ('api/room/', view_room.room_list, name='room_list'),
    path ('api/room_detail/<int:pk>/',  view_room.room_detail, name='room_detail'),
    path ('api/setup/', view_setup.setup_list, name='setup_list'),
    path ('api/setup_detail/<int:pk>/',  view_setup.setup_detail, name='setup_detail'),
]
 
urlpatterns += router.urls 