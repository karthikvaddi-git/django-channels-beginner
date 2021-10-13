from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json

class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    notification=models.TextField(max_length=100)
    is_seen=models.BooleanField(default=False)


    def save(self,*args,**kwargs):

        print("save called ")
        channellayer=get_channel_layer()
        nofnot=Notification.objects.filter(is_seen=False).count()
        data={'count':nofnot,'currentnotification':self.notification}
        async_to_sync(channellayer.group_send)
        ('test_group_name',{
            'type':'send_notification',
            'value':json.dumps(data)
        })
        super(Notification, self).save(*args, **kwargs)





