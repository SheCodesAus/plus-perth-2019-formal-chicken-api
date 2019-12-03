from rest_framework import serializers
from .models import Gift, Swap, Profile
from django.contrib.auth.models import User

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['gift_name', 'gift_description', 'gift_photo']
        
        # , 'gift_photo', 'date_added', 'sender']

class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swap
        fields = ['gift_id', 'recipient', 'match_date', 'gift_status', 'thank_you_message']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, required=False)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name','profile']