from rest_framework import serializers
from .models import Gift, Swap, Profile
from django.contrib.auth.models import User

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['gift_name', 'gift_description', 'gift_photo', 'sender_id']
        
        # , 'gift_photo', 'date_added', 'sender']

class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swap
        fields = ['id', 'gift_id', 'sender', 'recipient', 'match_date', 'gift_status', 'thank_you_message']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, required=False)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password','email', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        for f in UserSerializer.Meta.fields + UserSerializer.Meta.write_only_fields:
            set_attr(instance, f, validated_data[f])
        instance.set_password(validated_data['password'])
        user.set_password(password)
        instance.save()
        return instance