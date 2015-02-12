from django.db import models
from django.contrib.auth.models import User

class Rack(models.Model):
    number = models.IntegerField(null=True)
    def __str__(self):
        return self.number

class RackPosition(models.Model):
    number = models.IntegerField(null=True)
    def __str__(self):
        return self.number

class NetworkSpeed(models.Model):
    speed = models.CharField(max_length=20, help_text = '10G')
    def __str__(self):
        return self.speed

class NetworkSwitch(models.Model):
    hostname = models.CharField(max_length=45, help_text = 'arlab101')
    model_number = models.CharField(max_length=45, help_text = 'arlab101', null=True)
    speed = models.ForeignKey(NetworkSpeed)
    def __str__(self):
        return self.hostname + ': ' + self.speed
    
class Machine(models.Model):
    hostname = models.CharField(max_length=45, help_text = 'arlab101')
    owner = models.ForeignKey(User) #optional?
    description = models.CharField(max_length=45, help_text = 'Power Systems S822L') #optional?
    floor = models.IntegerField(null=True) 
    room = models.CharField(max_length=45,  help_text = '4F-8', blank=True, null=True) 
    
    rack = models.ForeignKey(Rack)
    rack_position = models.ForeignKey(RackPosition)
    network_switch = models.ForeignKey(NetworkSwitch)

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __str__(self):
        return self.hostname + ': ' + self.owner

