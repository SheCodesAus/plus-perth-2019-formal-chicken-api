import django_filters
from .models import Gift, Profile, Swap


class GiftFilter(django_filters.FilterSet):

    class Meta:
        model = Gift
        fields = {
            'gift_name' : ['icontains'],
            'sender': ['exact'],
        }

class SwapFilter(django_filters.FilterSet):

    class Meta:
        model = Swap
        fields = {
            'gift_id' : ['exact'],
            'sender': ['exact'],
            'recipient': ['exact'],
        }