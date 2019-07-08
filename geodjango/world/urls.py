from django.conf.urls import url
from . import views
from djgeojson.views import GeoJSONLayerView
#from world.views import MapsView
from . models import WorldBorder

app_name = 'world'
urlpatterns = [
        # /world/
        url(r'^$', views.index, name='index'),
        url(r'^maps/$', views.maps, name='maps'),
        url(r'^downloads/$', views.downloads, name='downloads'),
        url(r'^downloads/(?P<layer_name>.+)/$', views.fileDown, name='fileDown'),
        ###url(r'^maps/$', views.MapsView.as_view()),
        #url(r'^maps/$', GeoJSONLayerView.as_view(model=WorldBorder), name='maps3'),
        # /polls/
        #url(r'^$', views.IndexView.as_view(), name='index'),
        # /polls/5/
        #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # /polls/5/results
        #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        # /polls/5/vote
        #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]