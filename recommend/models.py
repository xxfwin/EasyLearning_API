# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Moodle user log table
class MdlLogstoreStandardLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=255)
    component = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    objecttable = models.CharField(max_length=50, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    crud = models.CharField(max_length=1)
    edulevel = models.IntegerField()
    contextid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    contextinstanceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    relateduserid = models.BigIntegerField(blank=True, null=True)
    anonymous = models.IntegerField()
    other = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    origin = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    realuserid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_logstore_standard_log'
        
class MdlCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    cacherev = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course'