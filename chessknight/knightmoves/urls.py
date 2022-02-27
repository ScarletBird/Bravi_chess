from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.RegisterChessPieceView.as_view(), name='register'),
    path('piece/<int:id>', views.DetailChessPieceView.as_view(), name='detail'),
]