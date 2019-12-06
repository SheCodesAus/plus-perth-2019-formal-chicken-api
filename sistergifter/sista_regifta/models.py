from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.signals import post_init
from django.core.mail import send_mail


User = get_user_model()


class Gift(models.Model):
    gift_name = models.CharField(max_length=50)
    gift_description = models.CharField(max_length=200)
    gift_photo = models.ImageField(upload_to='post_images', blank=True)
    # date_added = models.DateTimeField('date gift offered', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    gift_waiting = models.BooleanField('gift not yet matched', default=True)

    def __str__(self):
        return self.gift_name

    def get_old_gift(self):
        return Gift.objects.all().filter(gift_waiting = True).exclude(sender = self.sender).first()
    
    def save(self, *args, **kwargs):
        """ run on save """
        super().save(*args, **kwargs)
        # self.date_added =datetime.now()

        # Check to see if already matched
        if self.gift_waiting:
                new_gift= self
                old_gift = self.get_old_gift()
                create_swap(old_gift, new_gift)


# you probably want to turn on atomic transactions for this view.

                
def create_swap(old_gift, new_gift):
    newswap1 = Swap.objects.create(sender=old_gift.sender, recipient=new_gift.sender, gift_id =old_gift, gift_status ="", )
    newswap2 = Swap.objects.create(sender=new_gift.sender, recipient=old_gift.sender, gift_id =new_gift, gift_status ="", )
    newswap1.match_date = datetime.now()
    newswap2.match_date = datetime.now()
    new_gift.gift_waiting = False
    old_gift.gift_waiting = False
    newswap1.save()
    newswap2.save()
#     ##need to send emails here

#     send_mail(
#     'Sista Regifta Swap created',
#     'Your gift has been matched! Please post your gift to xxxx.',
#     'bigchick@sistaregifta.com',
#     ['item1.sender.email'],
#     fail_silently=False,
#     )




class Swap(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_swaps')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_swaps')
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    match_date = models.DateField('date match made', null= True, blank=True)
    date_sent = models.DateField('date gift sent', null=True, blank=True)
    gift_status = models.CharField(max_length=50)
    thank_you_message = models.CharField(null=True, blank=True, max_length=200)
    rating=models.IntegerField(null=True, blank=True, default=None)
   
    def __str__(self):
        return str(self.id)

             
    def save(self, *args, **kwargs):
        """ run on save """
        need_to_send_mail = self.id == None

        super().save(*args, **kwargs)

        if need_to_send_mail:
            send_mail(
            'Sista Regifta Swap created',
            'Your gift, '+ self.gift_id.gift_name + ' has been matched! Please post your gift to ' + self.recipient.first_name + ' ' + self.recipient.last_name + ' at ' + self.recipient.profile.address,
            'bigchick@sistaregifta.com',
            [self.sender.email],
            fail_silently=False,
            )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.user.username

