import requests
import numpy as np
import math
import string
import json
import pymongo
import urllib2
import time
from pymongo import MongoClient
from decimal import *
import matplotlib.pyplot as plt
import copy

##from sklearn.metrics.pairwise import cosine_similarity


start_time = time.time()
##client = MongoClient('localhost:27017')
##db = client.myfyp


##connection=MongoClient("ds1xxxxx.mlab.com", xxxxx)
##db1 = connection["database name"]
##db1.authenticate("username", "password")
##collection=db1["collection name"]

try:
   
    client = MongoClient('localhost:27017')

    db = client.myfyp
    #db1=client.tpp

except pymongo.error.ConnectionFailure,e:
    print "could not connect to MongoDB" %s %e




country_list=[db.nut_pakistani.find(),db.nut_indian.find(),db.nut_israeli.find(),db.nut_chinese.find(),db.nut_hong.find(),db.nut_korean.find()
              ,db.nut_japanese.find(),db.nut_italian.find(),db.nut_icelandic.find(),db.nut_swiss.find(),db.nut_austrian.find()
              ,db.nut_german.find(),db.nut_finnish.find(),db.nut_belgian.find(),db.nut_polish.find(),db.nut_australian.find(),db.nut_danish.find()
              ,db.nut_french.find(),db.nut_hungarian.find(),db.nut_russian.find(),db.nut_american.find(),db.nut_maltese.find(),db.nut_ukrainian.find()
              ,db.nut_romanian.find(),db.nut_portuguese.find(),db.nut_vietnamese.find(),db.nut_argentinian.find(),db.nut_greek.find(),db.nut_malaysian.find()
              ,db.nut_bulgarian.find(),db.nut_cambodian.find(),db.nut_thai.find(),db.nut_chilean.find(),db.nut_croatian.find(),db.nut_turkish.find(),db.nut_lao.find()
             ,db.nut_mexican.find(),db.nut_indonesian.find(),db.nut_saintlucian.find(),db.nut_iranian.find()
             ,db.nut_afghani.find(),db.nut_jordan.find(),db.nut_peruvian.find(),db.nut_moroccan.find(),db.nut_syrian.find()
             ,db.nut_ethiopian.find(),db.nut_bosnian.find(),db.nut_tunisian.find(),db.nut_egyptian.find(),db.nut_srilankan.find()
             ,db.nut_african.find()]

dia=[8.1,9.3,7.5,9.8,8.0,4.4,5.7,5.1,6.1,6.1,6.9,7.4,6.0,5.1,6.2,5.1,7.2,5.3,7.3,9.2,10.4,9.9,6.5,8.4,9.9,6.0,6.0,5.2,17.9,5.9,3.0,7.1,10.0,5.6,12.8,3.6
     ,15.8,6.5,10.9,10.1,8.8,11.7,6.9,8.1,8.1,3.4,9.9,9.6,16.7,8.0,6.3]
x1=input('Enter nutrient')
x0=input('Enter with')
app=[]
print len(country_list)
for i in range(len(country_list)):
    t=country_list.pop(0)
    print t
    x=0
    summ=0
    print i
    for p in t:
        
        i= p['nutritionEstimates']
        for line in i:
            if (line['attribute']=='ENERC_KCAL'):
                summ=summ+line['value']        
        
        x=x+1
##    print summ
##    print x

    tsum=summ/x
    app.append(tsum)
    #print 'avg neut val =',tsum
#print 'avg neut val =',app

iq=[84,82,95,105,108,106,104,102,101,101,100,99,99,99,99,98,98,98,98,97,98,97,97,94,95,94,93,92,91,93,91,91,90,90,90,89,88,87,62,84,84,84
    ,85,84,83,69,90,83,81,79,71]
print len(iq)
print len(dia)

q=['pak','ind','israel','chies','hong','korean','jap','itl','iceland','swis','aust','german','finish','bulg','polish','sutralia','danish','french','hungray','russia',
   'america','malta']
def covv(a,b):


    l=len(a)
    x=0
    y=0
    c= copy.deepcopy(a)
    d= copy.deepcopy(b)
    for i in range(len(a)):
        p1=c.pop(0)
        p2=d.pop(0)
        x=x+p1
        y=y+p2

    t1=float(x)/l
    t2=float(y)/l
    summ=0
    sumx=0
    sumy=0
    l1=len(a)-1
    for i in range(len(a)):
        p1=a.pop(0)
        p2=b.pop(0)

        e1=p1-t1
        es1=e1**2
        e2=p2-t2
        es2=e2**2
        ef1=e1*e2
        sumx=sumx+es1
        sumy=sumy+es2
        summ=summ+ef1

    sx=sumx/l1
    sy=sumy/l1
    sx=math.sqrt(sx)
    sy=math.sqrt(sy)


    cov=summ/l1
    mul=sx*sy
    cor=cov/mul
    
    
    return cor
x=covv(app,dia)    
print x
dic={'with':x0,"nutrient": x1,'correlation': x}
json=json.dumps(dic)
print dic
"putting data in database"
    
#collection.insert(dic)
    

