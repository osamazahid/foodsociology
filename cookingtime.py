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

##from sklearn.metrics.pairwise import cosine_similarity


start_time = time.time()
##client = MongoClient('localhost:27017')
##db = client.myfyp

##
##connection=MongoClient("ds1xxxxx.mlab.com", xxxxx)
##db1 = connection["sociology1"]
##db1.authenticate("user1", "user1")
##collection=db1["ibs_afghani"]

try:
   
    client = MongoClient('localhost:27017')

    db = client.myfyp

except pymongo.error.ConnectionFailure,e:
    print "could not connect to MongoDB" %s %e






##query=[db.pakistani.find_one(),db.indian.find_one(),db.arab.find_one()
##       ,db.chinese.find_one(),db.mongolian.find_one(),db.dutch.find_one()
##       ,db.cantonese.find_one(),db.afghani.find_one(),db.argentinian.find_one()
##       ,db.hong.find_one(),db.asian.find_one(),db.korean.find_one()
##       ,db.taiwanese.find_one(),db.japanese.find_one()]

query=[db.pakistani.find_one(),db.indian.find_one(),db.chinese.find_one()
       ,db.mongolian.find_one(),db.hong.find_one(),db.asian.find_one()
       ,db.korean.find_one(),db.taiwanese.find_one(),db.japanese.find_one()
       ,db.cantonese.find_one(),db.afghani.find_one(),db.argentinian.find_one()
       ,db.aruba.find_one(),db.canadian.find_one(),db.italianamerican.find_one()
       ,db.louisiana.find_one(),db.cajun.find_one(),db.american.find_one()
       ,db.basque.find_one(),db.french.find_one(),db.dutch.find_one()
       ,db.arab.find_one(),db.turkish.find_one(),db.welsh.find_one()
       ,db.latinamerican.find_one()]


query1=['pakistani','indian']

print query1
print '\n'
print len(query)
print len(query1)
inp=input('Enter Country Name    ')



mydoclist=[]

def makelist(que):
    x=0
    t=0

    i=[]
    d=[]
    for row in que['matches']:
        #print 'recipe name:'
        #print row['recipeName']
        i=row['totalTimeInSeconds']
        
        if(i!= None):
            #u=Decimal(i)
            f=float(i)/60
            t=t+f
            x=x+1
            
    r=t/x
    #print 'this result ',r
    return r
    
            

    

quer = [makelist(n) for n in query]
print quer
q=['pakistani','indian','chiese','mongoian','hong','asian','korean','taiwanese'
   ,'japanese','cantonese','afghani','argentanian','aruba','canadian'
   ,'italianamerican','lousiana','cajun','american','basque','french','dutch'
   ,'arab','turkish','welsh','latinamerica']
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
plt.plot(p, quer, 'ro')
plt.xticks(p, q, rotation='vertical')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
#plt.axis([0, 30, 0, 120])

plt.show()

##
###to remove extra bracket because of above line
##for i in quer:
##    quer=i
