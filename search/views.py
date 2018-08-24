# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

# import models for search module
from . import models
# queryset to dict funtions
from django.forms.models import model_to_dict

# import Doc2Vec packages
# initialize Dov2Vec model
import os
import gensim
import numpy as np
from gensim.models.doc2vec import Doc2Vec
TaggededDocument = gensim.models.doc2vec.TaggedDocument
model_dm = None


# import jieba for word segment, import re for html label filter
import jieba
import re
htmlfilter = re.compile(r'<[^>]+>',re.S)

# functions
# 
# index:
# return the info of this entry
# 
# getSimilarCourses:
# return the similar courses according to the query
# 
# updateCourses:
# call Doc2vec model to recalculate the representations of each course
# 

def index(request):
    return HttpResponse("This the API entry for search module.")
    
def getSimilarCourses(request):
    global model_dm
    if model_dm == None:
        if os.path.exists("./search/data/model_dm"):
            model_dm = Doc2Vec.load("./search/data/model_dm")
        else:
            updateCourses(request)
            #model_dm = Doc2Vec.load("./search/data/model_dm")
    
    segout = jieba.cut(request.GET.get('query'), cut_all=False)
    segstr = " ".join(segout)
    word_list = segstr.split(" ")
    inferred_vector_dm = model_dm.infer_vector(word_list)

    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)
    #return sims
    courseids = []
    for sim in sims:
        courseids.append(sim[0])
    
    courseinfo = models.MdlCourse.objects.using('datasrc').filter(id__in=courseids)
    
    returncourse = {}
    for ci in courseinfo:
        returncourse[model_to_dict(ci)['id']] = (model_to_dict(ci))
    # courseinfo = model_to_dict(courseinfo)
    
    return JsonResponse({"status":"0","data":returncourse})
    

def updateCourses(request):
    global model_dm
    x_train = get_datasest()
    model_dm = Doc2Vec(x_train, min_count=1, window = 5, vector_size = 50, sample=1e-3, workers=2)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=25)
    model_dm.save('./search/data/model_dm')
    
    if request != None:
        return JsonResponse({"status":"0","data":"update completed!"})
    else:
        return 0

def get_datasest():
    
    docs = models.MdlCourse.objects.using('datasrc').all().values_list("id","summary")
    #with open("./search/data/corpus.txt", 'r') as cf:
    #   docs = cf.readlines()
    #print docs

    x_train = []
    #y = np.concatenate(np.ones(len(docs)))
    #for i, text in enumerate(docs):
    for doc in docs:

        if doc[1] != None and doc[1] != "":
            
            text = htmlfilter.sub('',doc[1])

            segout = jieba.cut(text, cut_all=False)
            segstr = " ".join(segout)
            word_list = segstr.split(" ")

            document = TaggededDocument(word_list, [str(doc[0])])

            x_train.append(document)
            #print document
            #print doc[0]
    print (len(x_train))

    return x_train



    
    