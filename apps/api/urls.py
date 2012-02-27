from django.conf.urls.defaults import patterns,  url
from piston.resource import Resource
from apps.api.handlers import NodesHandler

class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt."""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

nodes_resource = CsrfExemptResource(handler=NodesHandler)

urlpatterns = patterns('',
    url(r'^nodes/$', nodes_resource),
)

