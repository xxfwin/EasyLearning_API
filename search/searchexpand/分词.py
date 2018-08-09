# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:14:17 2018

@author: Administrator
"""

from bs4 import BeautifulSoup 
import re
import urllib
import urllib.request
import requests
import pymysql 
url = "https://c.open.163.com/dwr/call/plaincall/OpenSearchBean.searchCourse.dwr"
"print(url)"
payload = {
        'callCount':'1',
        'scriptSessionId':'${scriptSessionId}190',
        'httpSessionId':'',
        'c0-scriptName':'OpenSearchBean',
        'c0-methodName':'searchCourse',
        'c0-id':'0',
        'c0-param0':'ted',
        'c0-param1':'1',
        'c0-param2':'1000',
        'batchId':'1522487268711',
 }

req=requests.post(url, data=payload)
req.encoding=req.apparent_encoding
req=req.text
soup = BeautifulSoup(req,'lxml')
m=re.findall(r'description=".*"',req)
n=re.findall(r'title=".*"',req)
f = open('D:/spy_data/test.txt','w')  
for i in range (2,999):   
    m[i]=m[i].encode('utf-8').decode('unicode_escape')
    m[i]=m[i][:m[i].index(";")]
    m[i]=re.sub("[A-Za-z0-9]", "", m[i])
    m[i] = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）{}：=]+", "",m[i])
    n[i]=n[i].encode('utf-8').decode('unicode_escape')
    n[i]=re.sub("[A-Za-z0-9]", "", n[i])
    n[i] = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）{}：=【】]+", "",n[i])
    f.write(m[i]+'\n')  
    f.write(n[i]+'\n')
f.close
