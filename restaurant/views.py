from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Booking, MenuItem
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import render
from .permissions import IsManager

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    filterset_fields = ['price']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsManager | IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    
class SingleMenuItemView(generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsManager | IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions() 
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 