from django.shortcuts import render
from rest_framework import viewsets      
from .serializers import GiftSerializer, SwapSerializer, UserSerializer      
from .models import Gift, Swap, Profile                     
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class GiftView(viewsets.ModelViewSet):       
    serializer_class = GiftSerializer         
    queryset = Gift.objects.all()
    
    class Meta:
        ordering = ['-id']      


class SwapView(viewsets.ModelViewSet):       
    serializer_class = SwapSerializer         
    queryset = Swap.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

 