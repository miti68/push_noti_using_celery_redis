# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

# STORE THE USERS'S DEVICE INFORMATION WHERE THE NOTIFICATION WILL BE SENT
class MobileDevice(models.Model): 
    participant = models.OneToOneField(User, related_name='device', on_delete=CASCADE)
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    token = models.TextField()

# STORE DATA ABOUT THE INFORMATION TO DELIVER
class MobileNotification(TimeStampedModel):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')

# reflects the interaction between two users of the app
class InAppMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=CASCADE)
    content = models.CharField(max_length=512)
