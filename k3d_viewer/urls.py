from django.conf.urls import *
from views import *

#from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$',views.main, name='main'),
    url(r'^selector/$',views.selector,name='selector'),
    url(r'^info_view/$',views.info_view,name='info_view'),
    url(r'^search_list/$',views.search_list,name='search_list'),
]


