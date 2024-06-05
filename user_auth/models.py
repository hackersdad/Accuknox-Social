# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class SocialUser(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        db_table = 'social_user'

class FriendRequest(models.Model):
    from_user_id = models.IntegerField()
    to_user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        db_table = 'friend_request'

class Friendship(models.Model):
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'friendship'

class LoginRecord(models.Model):
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255)

    class Meta:
        db_table = 'login_record'
