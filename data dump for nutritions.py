import requests
import json
import pymongo
import urllib2
import time
from pymongo import MongoClient
from decimal import *
start_time = time.time()


#Connection with mlab cloud


##connection=MongoClient("ds1xxxxx.mlab.com", xxxxx)
##db1 = connection["sociology1"]
##db1.authenticate("username", "password")
##collection=db1["name of collection"]


#connection with local mongo server
try:
   
    client = MongoClient('localhost:27017')

    db = client.myfyp
    #db1=client.tpp

except pymongo.error.ConnectionFailure,e:
    print "could not connect to MongoDB" %s %e





# query to find collection of country
# to fetch recipes

query=[db.lao.find_one()]#input


mydoclist=[]


#function to find recipe id to find nutrients
def makelist(que):
    x=0
    t=0

    m=[]
    d=[]
    for row in que['matches']:
        #print 'recipe name:'
        #print row['recipeName']
        i=row['id']
        p=i.encode('UTF8')
        
        m.append(p)
        x=x+1
    print x
    return m
        
 

    

quer = [makelist(n) for n in query]



#to remove extra bracket because of above line
for i in quer:
    quer=i
l=0
for j in quer:
    
    #n=quer.pop(x)
    
  
    #creation of url from recipe id
    search_base='http://api.yummly.com/v1/api/recipe/'
    key='INSERT YOUR KEY HERE'
    t=search_base+j+key
    r= requests.get(t)
    x=r.json()

    print x

    #query to dump nutritional data in mongo
    #db.nut_lao.insert(x)
    print 'putted',l

print 'job done'
##x=0
##for p in db.nut_israeli.find():
##    print p['name']
##    x=x+1
##    print x


