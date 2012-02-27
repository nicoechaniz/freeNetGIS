# Create your views here.

from apps.nodes.models import Node
from django.shortcuts import render_to_response

def index(request):
    """
    Home of the maps application
    """
    latest_node_list = Node.objects.all().order_by('-updated_date')[:5]
    return render_to_response('maps/index.html', {'latest_node_list': latest_node_list})


