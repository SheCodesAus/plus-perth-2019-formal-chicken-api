from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.signals import post_init


User = get_user_model()


all_gifts = []

class Gift(models.Model):
    gift_name = models.CharField(max_length=50)
    gift_description = models.CharField(max_length=200)
    gift_photo = models.ImageField(upload_to='post_images', blank=True)
    # date_added = models.DateTimeField(verbose_name='date gift offered', default=datetime.now, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    gift_waiting = models.BooleanField(default=True)

    def __str__(self):
        return self.gift_name
    
    def save(self, *args, **kwargs):
        """ run on save """
        super().save(*args, **kwargs)

        # Check to see if already matched
        if self.gift_waiting:
            #If not matched check for match
            old_gift = super().objects.filter(gift_waiting = True).exclude(sender =self.sender).first()
            if old_gift:
                #create swap
                create_swap(old_gift, self)


                
def create_swap(item1, item2):
    newswap1 = Swap.objects.create(sender=item1.sender, recipient=item2.sender, gift_id =item1, gift_status ="", )
    newswap2 = Swap.objects.create(sender=item2.sender, recipient=item1.sender, gift_id =item2, gift_status ="", )
    newswap1.match_date = datetime.now()
    newswap2.match_date = datetime.now()
    item1.gift_waiting = False
    item2.gift_waiting = False
    item1.save()
    item2.save()



class Swap(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_swaps')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_swaps')
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    match_date = models.DateField('date match made', null= True, blank=True)
    date_sent = models.DateField('date gift sent', null=True, blank=True)
    gift_status = models.CharField(max_length=50)
    thank_you_message = models.CharField(null=True, blank=True, max_length=200)
    rating=models.IntegerField(null=True, default=None)
   
    def __str__(self):
        return self.swap_id


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

