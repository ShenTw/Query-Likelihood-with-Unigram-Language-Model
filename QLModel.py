# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:02:20 2017

@author: shen
"""

#!/usr/bin/env python

"""The simplest TF-IDF library imaginable.
Add your documents as two-element lists `[docname,
[list_of_words_in_the_document]]` with `addDocument(docname, list_of_words)`.
Get a list of all the `[docname, similarity_score]` pairs relative to a
document by calling `similarities([list_of_words])`.
See the README for a usage example.
"""
import math
class QLM:
    def __init__(self):
        self.weighted = False
        self.documents = {}
        self.corpus_dict = {}
        self.sims = {}
        self.a = 0.5
    def add_document(self, doc_name, list_of_words):
        # building a dictionary
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(w, 0.) + 1.0
        # 計算完每個字的次數
        length = float(len(list_of_words))
        # 處理頻率(除上該文章字數)
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length
          #其中一種作法  doc_dict[k] = 1 + doc_dict[k] / length
           # QLM中似乎用不到整個字典的字
        self.documents[doc_name]= doc_dict
    def likelihood(self, list_of_words, queryName):
        """Returns a list of all the [docname, similarity_score] pairs relative to a
list of words.
        """

        # building the query dictionary
        #print(self.corpus_dict)
        query_dict = {}
        for w in list_of_words:
            if query_dict.get(w,0)==0:
                query_dict[w] = query_dict.get(w, 0.0) + 1.0
        """ test for query_dict
        for w in query_dict:
            print(w)
        """
        # computing the list of similarities
        QLMDic = {}
        for doc in self.documents:
            #每一篇文件要做的事情
            #1. 讀出名字跟dic
            #2. 與query比對是否存在該字,有的話計算存下字典中，該字出現的機率值並相乘 沒有則不做 ,存在暫存值中
            #3. 把Likelihood中的值相乘所得到最後的值，並配合Doc名放到QLMDic中
            #4. 對QLMDic做排序    
            
            queryLikelihood= 0.0
            #1 得到該document的字典 {}
            dicTemp = self.documents[doc]
            
            #2.
            for w in query_dict:
                        queryLikelihood = math.log(self.a*dicTemp.get(w,0.0)+(1-self.a)*float(self.corpus_dict[str(int(w))]))+queryLikelihood
                       
                    
            #3.
            
            QLMDic[doc] = queryLikelihood
    
        #4.    
        self.sims[queryName] = sorted(QLMDic.items(), key=lambda d:d[1], reverse = True)
        #做排序    
         