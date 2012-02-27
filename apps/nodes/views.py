# Create your views here.

from apps.nodes.models import Node
from django.contrib.gis.feeds import Feed
from django.core import serializers
from django.http import HttpResponse

class LatestNodesFeed(Feed):
    title = "Ultimos nodos"
    link = "/lista_nodos/"
    description = "Ultimos nodos modificados"

    def items(self):
        return Node.objects.order_by('-updated_date')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.address

    def item_geometry(self, item):
        return item.ubication

def json(request):
    """
    Returns a json list with all the nodes
    """
    nodes = serializers.serialize("geojson", Node.objects.all())

    return HttpResponse(nodes, mimetype='application/json')

