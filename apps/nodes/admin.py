from django.contrib.gis import admin
from apps.nodes.models import Node
from apps.devices.models import Wireless

class WirelessInline(admin.StackedInline):
    model = Wireless
    extra = 1
    
class NodeAdmin(admin.GeoModelAdmin):
    inlines = [WirelessInline]
    list_display = ('name', 'updated_date', 'antenna_elevation')
    list_filter = ['updated_date']   
    

admin.site.register(Node, NodeAdmin)