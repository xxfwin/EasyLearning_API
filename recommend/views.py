# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

# import Count support
from django.db.models import Count

# import models for search module
from . import models
# queryset to dict funtions
from django.forms.models import model_to_dict

# import CF model
import sys
sys.path.append('../')
from lib.CF import CF

import time

# shared vars
recom = None

def index(request):
    return HttpResponse("This the API entry for recommend module.")


def getRecommendCourses(request):
    global recom
    if recom == None:
        updateRecommendCourses(None)
    recom.recommendByUser(int(request.GET.get('userid')))
    
    # use recommend course id to query course info
    courseids = []
    for recommendinstance in recom.recommendList:
        courseids.append(recommendinstance[1])
    
    courseinfo = models.MdlCourse.objects.using('datasrc').filter(id__in=courseids)
    
    returncourse = {}
    for ci in courseinfo:
        returncourse[model_to_dict(ci)['id']] = (model_to_dict(ci))
    # courseinfo = model_to_dict(courseinfo)
    
    return JsonResponse({"status":"0","data":returncourse})
    
    
def updateRecommendCourses(request):
    global recom
    # Dest sql ->> select userid,courseid, count(courseid) from mdl_logstore_standard_log where eventname = '\\core\\event\\course_viewed' and userid != 0 group by userid,courseid;
    records = models.MdlLogstoreStandardLog.objects.using('datasrc').filter(eventname__exact='\\core\\event\\course_viewed').exclude(userid__exact=0).all().values_list("userid","courseid")
    ratingdata = records.annotate(sumcourse = Count('courseid')).values_list('userid','courseid','sumcourse')
    
    coursedata = models.MdlCourse.objects.using('datasrc').values_list('id')
    
    courselist = []
    ratinglist = []
    
    for course in coursedata:
        courselist.append([course])
    for rating in ratingdata:
        ratinglist.append([rating[0], rating[1], rating[2]])
    recom = CF(courselist, ratinglist, k=20)
    return JsonResponse({"status":"0","data":"update completed!"})