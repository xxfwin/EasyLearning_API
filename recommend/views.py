# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse
# Create your views here.

def index(request):
    return HttpResponse("This the API entry for recommend module.")


def getRecommendCourses(request):
    
    return JsonResponse({"status":"0","data":"In development"})