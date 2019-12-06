from django.shortcuts import render, redirect
from rest_framework import viewsets      
from .serializers import GiftSerializer, SwapSerializer, UserSerializer, ProfileSerializer      
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

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the gifts
    #     for which the currently authenticated user is the sender.
    #     """
    #     User = self.request.sender
    #     return Gift.objects.filter(sender=User)  


        # def get_queryset(self):
        #     """
        #     This view should return a list of all the purchases for
        #     the user as determined by the username portion of the URL.
        #     """
        #     sender = self.kwargs['sender']
        #     return Gift.objects.filter(sender=sender)


class SwapView(viewsets.ModelViewSet):       
    serializer_class = SwapSerializer         
    queryset = Swap.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

 
# send_mail(
#         'Sista Regifta Swap created',
#         'Your gift has been matched! Please post your gift to xxxx.',
#         'bigchick@sistaregifta.com',
#         ['swap.sender.email'],
#         fail_silently=False,
#         )

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
