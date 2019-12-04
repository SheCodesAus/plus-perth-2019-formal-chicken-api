from rest_framework import serializers
from .models import Gift, Swap, Profile

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['gift_name', 'gift_description', 'gift_photo', 'sender_id']
        
        # , 'gift_photo', 'date_added', 'sender']



class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swap
        fields = ['gift_id', 'sender', 'recipient', 'match_date', 'gift_status', 'thank_you_message']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email']