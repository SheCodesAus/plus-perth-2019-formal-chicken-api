from django.shortcuts import render
from rest_framework import viewsets      
from .serializers import GiftSerializer, SwapSerializer      
from .models import Gift, Swap, Profile                     
  

class GiftView(viewsets.ModelViewSet):       
    serializer_class = GiftSerializer         
    queryset = Gift.objects.all()              

class SwapView(viewsets.ModelViewSet):       
    serializer_class = SwapSerializer         
    queryset = Swap.objects.all()    