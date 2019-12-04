from django.shortcuts import render, redirect
from rest_framework import viewsets      
from .serializers import GiftSerializer, SwapSerializer, ProfileSerializer      
from .models import Gift, Swap, Profile 
from django.core.mail import send_mail
from django.conf import settings

  

class GiftView(viewsets.ModelViewSet):       
    serializer_class = GiftSerializer         
    queryset = Gift.objects.all()            

class SwapView(viewsets.ModelViewSet):       
    serializer_class = SwapSerializer         
    queryset = Swap.objects.all()    

class ProfileView(viewsets.ModelViewSet):       
    serializer_class = ProfileSerializer         
    queryset = Profile.objects.all()  


# send_mail(
#     'Test message2',
#     'Well I will be very suprised if this works.',
#     'bigchick@sistaregifta.com',
#     ['email@test.com'],
#     fail_silently=False,
# )

# send_mail(
#     'Anna is a Django wiz',
#     "Well this is a fun automated message from Anna's app. Please enjoy it",
#     'bigchick@sistaregifta.com',
#     ['email@test.com'],
#     fail_silently=False,
# )
