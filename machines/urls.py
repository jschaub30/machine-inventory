from django.conf.urls import patterns
from machines.views import RackList

urlpatterns = patterns('',
    (r'^racks/$', RackList.as_view()),
)
