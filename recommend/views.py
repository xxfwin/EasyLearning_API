# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

# import Count support
from django.db.models import Count

# import models for search module
from . import models
# import CF model
import sys
sys.path.append('../')
from lib.CF import CF

import time

def index(request):
    return HttpResponse("This the API entry for recommend module.")


def getRecommendCourses(request):
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
        
     
    # -------------------------start recommend-------------------------------
    start = time.clock()
    recom = CF(courselist, ratinglist, k=20)
    recom.recommendByUser(int(request.GET.get('userid')))
    print recom.recommendList
    
    
    return JsonResponse({"status":"0","data":recom.recommendList})
    
def updateRecommendCourses(request):
    
    return JsonResponse({"status":"0","data":"update completed!"})