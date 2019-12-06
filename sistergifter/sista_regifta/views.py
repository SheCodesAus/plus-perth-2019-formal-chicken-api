from django.shortcuts import render, redirect
from rest_framework import viewsets      
from .serializers import GiftSerializer, SwapSerializer, UserSerializer      
from .models import Gift, Swap, Profile                     
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings


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
    # permission_classes = (IsAuthenticated,)

 
# send_mail(
#     'Test message2',
#     'Well I will be very suprised if this works.',
#     'bigchick@sistaregifta.com',
#     ['email@test.com'],
#     fail_silently=False,
# )

#     "Well this is a fun automated message from Anna's app. Please enjoy it",
# send_mail(
#     'Anna is a Django wiz',
#     'bigchick@sistaregifta.com',
#     ['email@test.com'],
#     fail_silently=False,
# )
