from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']