import requests
import numpy as np
import math
import string
import json
import pymongo
import copy
from pymongo import MongoClient
##from sklearn.metrics.pairwise import cosine_similarity



##client = MongoClient('localhost:27017')
##db = client.myfyp

try:
    
    client = MongoClient('localhost:27017')
    db = client.myfyp
except pymongo.error.ConnectionFailure,e:
    print "could not connect to MongoDB" %s %e


query=[db.pakistani.find_one(),db.indian.find_one(),db.chinese.find_one()]
query1=['pakistani','indian','chinese']

mydoclist=[]

def makelist(que):
    ##w=input('input enter food collection')
    ##w=db.food00.find_one()
    i=[]
    d=[]
    for row in que['matches']:
        #print 'recipe name:'
        #print row['recipeName']
        i=row['ingredients']
        p=[x.encode('UTF8') for x in i]#to remove 'u' from json data
        #o=' '.join(p)
        z=[q.replace(" ", "")  for q in p] #to remove spaces b/w two letter word in list
        o=' '.join(z)# concatinating each recipe ingrediant list seperatly
        o=str(o)
        o=' '+o

        
        d.append(o)

    e=' '.join(d)#concatinate all recipes to make a string
    
    
    mydoclist.append(e)
    return mydoclist


quer = [makelist(n) for n in query]

#to remove extra bracket because of above line
for i in quer:
    quer=i

#############################################
#print quer

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
  return freq(term, document)

def freq(term, document):
  return document.split().count(term)

vocabulary = build_lexicon(quer)

doc_term_matrix = []
#print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'

vocabulary1=', '.join(list(vocabulary))

z=vocabulary1.replace(",", "")

for doc in quer:
    #print 'The doc is "' + doc + '"'
    tf_vector = [tf(word, doc) for word in vocabulary]
##    tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
##    print 'The tf vector for Document %d is [%s]' % ((quer.index(doc)+1), tf_vector_string)
    doc_term_matrix.append(tf_vector)
    
    # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
    # try it!  type(mydoclist.index(doc) + 1)

print 'All combined, here is our master document term matrix: '
#print doc_term_matrix

p=z.split()




we=0

def check_zero(num):
    app=[]
    for i in range(len(num)):
        if (num[i]==0):
            app.append(i)
    return app


aplis0=[]
aplis1=[]

#loop to remove entries which are 0
for x in doc_term_matrix:
    #print 'lenth of string',len(x)
    repp=copy.deepcopy(p)     #deep copying bcz list update itself after every pop or del
    
    ew=0    
    #ret=check_zero(x)
    
    for l in range(len(x)):
         
         if (x[ew]==0):
             del x[ew]
             del repp[ew]
         else:
                ew=ew+1
    print 'lopp run '
    
    aplis0.append(x)
    aplis1.append(repp)
    
    
    print 'success print'
    
summ=0
sumo=[]

#sum used for findig persontage
for x in doc_term_matrix:
    for i in range (len(x)):
        summ=summ+x[i]
    sumo.append(summ)
print 'sum is =',sumo


#loop to find max val in list and its index
for i in range(len(aplis0)):
    x=aplis0.pop(0)
    t=aplis1.pop(0)
    op=sumo.pop(0)
    
    print query1[i]
    for i in range(5):
        maxval=max(x)
        maxindex=x.index(maxval)
        print 'Number of time Ingrediant used'+'  ',maxval
        it=(float(maxval)/op)*100
        print 'percentage of maxval',it
        print 'index number=',maxindex
        print 'Recipe Name==>',t[maxindex]
        x.pop(maxindex)
        t.pop(maxindex)
            
    #we=we+1
    


