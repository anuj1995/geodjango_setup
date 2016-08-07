from django.conf.urls import url
from . import views
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
# from  import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.mappage, name=''),
    url(r'^mapInteractive/$', views.mapInteractive, name='mapInteractive'),
    url(r'^mapInteractive/create/$', views.interestPointCreate),
    url(r'^mapInteractive/edit/$', views.interestPointEdit),
    url(r'^mapOperation/$', views.mapOperation, name='mapOperation'),
]

urlpatterns += staticfiles_urlpatterns()
