# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:27:14 2018

@author: Administrator
"""
# -*- coding: utf-8 -*-
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
for i in range (2,999):   
    m[i]=m[i].encode('utf-8').decode('unicode_escape')
    m[i]=m[i][:m[i].index(";")]
    n[i]=n[i].encode('utf-8').decode('unicode_escape')
"""#2.插入操作  
db= pymysql.connect(host="localhost",user="root",  
    password="12345678",db="world",port=3306,use_unicode=True, charset="utf8")    
# 使用cursor()方法获取操作游标  
cur = db.cursor()
for i in range (2,999):   
    sql_insert =("insert into search1(id,coursename,content) values({}, '{}', '{}')".format(i,n[i],m[i]))  
    cur.execute(sql_insert)  
    #提交  
    db.commit()   
db.close()"""




 


