from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from apps.nodes.models import Node
from apps.nodes.views import LatestNodesFeed

''' Url config of feeds based on django 1.1, because
    django.contrib.gis.feeds have the old style.
'''

feeds = {
    'latest': LatestNodesFeed,
}

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Node.objects.order_by('-updated_date')[:5],
            context_object_name='latest_nodes_list')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
                model=Node)),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
    url(r'^json', 'apps.nodes.views.json'),
)
