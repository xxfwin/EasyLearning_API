# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

# import Doc2Vec packages
# initialize Dov2Vec model
import os
import gensim
import numpy as np
from gensim.models.doc2vec import Doc2Vec
TaggededDocument = gensim.models.doc2vec.TaggedDocument
model_dm = None

# import jieba for word segment
import jieba

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
    
    inferred_vector_dm = model_dm.infer_vector(request.GET.get('query'))
    #print (inferred_vector_dm)
    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)
    #return sims
    
    return JsonResponse({"status":"0","data":sims})

def updateCourses(request):
    global model_dm
    x_train = get_datasest()
    model_dm = Doc2Vec(x_train,min_count=1, window = 3, vector_size = 100, sample=1e-3, negative=5, workers=2)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=10)
    model_dm.save('./search/data/model_dm')
    
    if request != None:
        return JsonResponse({"status":"0","data":"update completed!"})
    else:
        return 0

def get_datasest():
    with open("./search/data/corpus.txt", 'r') as cf:
        docs = cf.readlines()

    x_train = []
    #y = np.concatenate(np.ones(len(docs)))
    for i, text in enumerate(docs):
        segout = jieba.cut(text, cut_all=False)
        segstr = ' '.join(segout)
        word_list = segstr.split(" ")
        l = len(word_list)
        word_list[l-1] = word_list[l-1].strip()
        document = TaggededDocument(word_list, tags=[i])
        x_train.append(document)

    return x_train



    
    