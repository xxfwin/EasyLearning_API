# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:28:26 2018

@author: Administrator
"""

# coding:utf-8

import gensim
import numpy as np
from gensim.models.doc2vec import Doc2Vec

TaggededDocument = gensim.models.doc2vec.TaggedDocument

def get_datasest():
    with open("D:/spy_data/test1.txt", 'r', encoding='utf-8') as cf:
        docs = cf.readlines()
        print (len(docs))

    x_train = []
    #y = np.concatenate(np.ones(len(docs)))
    for i, text in enumerate(docs):
        word_list = text.split(' ')
        l = len(word_list)
        word_list[l-1] = word_list[l-1].strip()
        document = TaggededDocument(word_list, tags=[i])
        x_train.append(document)

    return x_train

def getVecs(model, corpus, size):
    vecs = [np.array(model.docvecs[z.tags[0]].reshape(1, size)) for z in corpus]
    return np.concatenate(vecs)

def train(x_train, size=500, epoch_num=1):
    model_dm = Doc2Vec(x_train,min_count=1, window = 3, size = size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=70)
    model_dm.save('D:/spy_data/model_dm')

    return model_dm


def test():
    model_dm = Doc2Vec.load("D:/spy_data/model_dm")
    test_text = ['网络暴力']
    inferred_vector_dm = model_dm.infer_vector(test_text)
    print (inferred_vector_dm)
    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)
    return sims

if __name__ == '__main__':
    x_train = get_datasest()
    model_dm = train(x_train)

    sims = test()
    for count, sim in sims:
        sentence = x_train[count]
        words = ''
        for word in sentence[0]:
            words = words + word + ' '
        file = open("word_1.txt",'a')
        file.write(words+'\n')
    file.close()
       
   
