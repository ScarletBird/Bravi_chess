
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from knightmoves.api import viewsets

route = routers.DefaultRouter()
route.register(r'pieces', viewsets.ChessPieceViewSet, basename="Pieces")
route.register(r'moves', viewsets.ChessMovesViewSet, basename="Moves")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('knightmoves.urls')),
    path('api/v1/', include(route.urls))
]
