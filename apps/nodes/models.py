# -*- coding: utf-8 -*-
#from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Node(models.Model):
    name = models.CharField(max_length=70)
    creation_date = models.DateTimeField(verbose_name=_(u"Created Date"))
    updated_date = models.DateTimeField(verbose_name=_(u"Updated Date"))
    address = models.TextField()
    antenna_elevation = models.FloatField()
    ubication = models.PointField(blank=True, null=True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/nodes/%i/" % self.id