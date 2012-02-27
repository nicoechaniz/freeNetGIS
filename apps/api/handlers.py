import re
from piston.handler import BaseHandler
from piston.utils import rc, throttle

from apps.nodes.models import Node

class NodesHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Node

    def read(self, request):
        nodes = Node.objects.all()

        if nodes:
            return nodes
        else:
            return rc.NOT_FOUND

