# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

import sys
import os


import smt_process.detect_class as detect_class

import cv2
import numpy as np

# change below to your DATA_PATH and DP_ROOT
DP_ROOT='/home/junwon/smt-project/SMT/detect_part/'

menu={}
components={}

def progressbar_callback(msg, i, m):
    """
    Callback to display a text based progress bar when loading,
     storing or performing any other lengthy operation.

    :param msg: Message to be displayed
    :param i: Current value
    :param m: Maximal value
    :return:
    """
    print msg,
    x = int(100 * float(i) / m)
    print "#" * (x / 2),
    print "[%2d%%]" % x,
    print "-" * (50 - x / 2),
    print "\r",
    sys.stdout.flush()



def index(request):
    return render(request, 'model_viewer/index.html',{})

def main(request, comp):
    global components
    components = comp

    return render(request, 'model_viewer/main.html',locals())

def selector(request):
    global menu

    model_list = [f for f in os.listdir(DP_ROOT) if f.endswith('model')]   

    for f in model_list:
        menu[f] = f

    return render(request, 'model_viewer/selector.html',{'menu':menu})

def info_view(request):
    
    key= None
    q = None
    content = None

    print "<<info_view>>"
    if 'key' in request.GET:
        key = request.GET['key']


    if 'q' in request.GET:
        q = request.GET['q']


    if key is not None and q is not None:
        content = components[key]
    
    return render(request, 'model_viewer/info_view.html',{'q':q,'key':key,'content':content})

def search_list(request):
    q=None
    key_list=[]
    all_list=[]
    global components
    print "<< search list section>>"
    if 'q' in request.GET:
        q= request.GET['q']
        print 'q:', q
        q= menu[q]
        model = os.path.join(DP_ROOT,q)

  #      DC = detect_class.ComponentDetector()
  #      DC.get_components_from_pickle(model,callback=progressbar_callback)

   #     components = DC.known_components

        
        for key in components:
                key_list.append(key)

    return render(request, 'model_viewer/search_list.html',{'q':q,'menu':menu,'key_list':key_list})
