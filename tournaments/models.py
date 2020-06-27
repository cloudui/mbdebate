from django.db import models


from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse 

from users.models import CustomUser

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=10, null=True)
    enddate = models.CharField(max_length=10, null=True)
    cost = models.FloatField(null=True)
    link = models.CharField(max_length=50, null=True)

    location = models.CharField(max_length=50, null=True)
    
    is_payment_due = models.BooleanField(default=False)
    

    
    slug = models.SlugField(null=False, unique=True, default=None)

    users = models.ManyToManyField(CustomUser,blank=True) # through payment

    


    def show_users(self):
        return ', '.join([a.email for a in self.users.all()])

    @classmethod
    def register(cls, user, tournament):
        tournament.users.add(user)

    @classmethod
    def unregister(cls, user, tournament):
        tournament.users.remove(user)

  

    def __str__(self):
        return self.name

   

# class Payment(models.Model):
#     total_cost = models.FloatField(null=True)
    
#     transportation_cost = models.FloatField(null=True)

#     lodging_cost = models.FloatField(null=True)

#     registration_fee = models.FloatField(null=True)

