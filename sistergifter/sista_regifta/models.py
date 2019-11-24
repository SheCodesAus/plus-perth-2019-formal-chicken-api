from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()



class Gift(models.Model):
    gift_name = models.CharField(max_length=50)
    gift_description = models.CharField(max_length=200)
    gift_photo = models.ImageField(upload_to='post_images', blank=True)
    # date_added = models.DateTimeField(verbose_name='date gift offered', default=datetime.now, blank=True)
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift_name


class Swap(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_swaps')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_swaps')
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    match_date = models.DateField('date match made')
    date_sent = models.DateField('date gift posted')
    gift_status = models.CharField(max_length=50)
    thank_you_message = models.CharField(max_length=200)
    rating=models.IntegerField(null=True, default=None)
   
    def __str__(self):
        return self.swap_id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    # def category_names(self):
    #     all_names = ""
    #     for cat in self.categories.all():
    #         all_names = all_names + str(cat) + ", "
            
    #     if len(all_names)==0:
    #         return "categories unknown"
        
    #     return all_names[0:-2]
