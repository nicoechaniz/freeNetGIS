from django.db import models
from apps.devices.constants import *

# Create your models here.
class Wireless(models.Model):
    name = models.CharField(max_length=70)
    node = models.ForeignKey('nodes.Node')
    radio_model = models.ForeignKey('RadioModel')
    mac_address = models.CharField(max_length=17)
    serial_number = models.CharField(max_length=70)
    radio_mode = models.CharField(max_length=2, choices=RADIO_MODE)    
    protocol = models.CharField(max_length=2, choices=PROTOCOL_CHANNELS)  
    accept_clients = models.BooleanField()
    antenna = models.ForeignKey('Antenna')
    
    def __unicode__(self):
        return self.name  
        
    class Meta:
        verbose_name = 'Wireless Device'
        verbose_name_plural = 'Wireless Devices'
      
    
class RadioModel(models.Model):
    name = models.CharField(max_length=70)
    firmware = models.ForeignKey('Firmware')
    
    def __unicode__(self):
        return self.name      
    
class Firmware(models.Model):
    name = models.CharField(max_length=70)
    
    def __unicode__(self):
        return self.name      
        
class Antenna(models.Model):
    name = models.CharField(max_length=70)
    serial_number = models.CharField(max_length=70)
    type = models.CharField(max_length=2, choices=ANTENNA_TYPE)
    gain = models.IntegerField()
    degrees = models.IntegerField()
    connector =  models.CharField(max_length=2, choices=CONNECTOR_TYPE)
    
    def __unicode__(self):
        return self.name
    
class Server(models.Model):
    name = models.CharField(max_length=70)
    node = models.ForeignKey('nodes.Node')
    
    