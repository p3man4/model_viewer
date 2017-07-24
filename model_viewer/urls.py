from django.conf.urls import *
from views import *

#from django.conf.urls import url

from . import views

def progressbar_callback(msg,i,m):
    print msg,
    x = int(100 * float(i) / m)
    print "#" * (x/2),
    print "[%2d%%]" % x,
    print "-" * (50 - x/ 2),
    print "\r",
    sys.stdout.flush()



import os
import smt_process.detect_class as detect_class
DP_ROOT='/home/junwon/smt-project/SMT/detect_part/'

model_list = [f for f in os.listdir(DP_ROOT) if f.endswith('model')]

model= os.path.join(DP_ROOT,model_list[0])
print "model:",model
DC = detect_class.ComponentDetector()
DC.get_components_from_pickle(model,callback=progressbar_callback)
components = DC.known_components


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$',views.main,{'comp':components}, name='main'),
    url(r'^selector/$',views.selector,name='selector'),
    url(r'^info_view/$',views.info_view,name='info_view'),
    url(r'^search_list/$',views.search_list,name='search_list'),
]


