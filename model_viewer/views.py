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

# change DP_ROOT as needed
DP_ROOT='/home/junwon/smt-project/SMT/detect_part/'

menu={}
components={}


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

    img_box={}

    if key is not None and q is not None:
        content = components[key]
        for i,v in enumerate(content['instances']):
            img_iso = v['isolated_component']
            cv2.imwrite('./model_viewer/static/model_viewer/' + str(i) +'_iso.png',img_iso)

            img_hs = v['hs_histogram']
            cv2.imwrite('./model_viewer/static/model_viewer/' + str(i) + '_hs.png',img_hs)

            img_gray = v['img_gray']
            cv2.imwrite('./model_viewer/static/model_viewer/' + str(i)+ '_gray.png',img_gray)
            
            img_bgr = v['img_bgr']
            cv2.imwrite('./model_viewer/static/model_viewer/' + str(i) + '_bgr.png',img_bgr)
           




                




    return render(request, 'model_viewer/info_view_v2.html',{'q':q,'key':key,'content':content})

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
        
        for key in components:
                key_list.append(key)

    return render(request, 'model_viewer/search_list.html',{'q':q,'menu':menu,'key_list':key_list})
