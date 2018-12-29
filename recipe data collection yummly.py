import requests
import json
import pymongo
from pymongo import MongoClient

#creation of api url
search_base='http://api.yummly.com/v1/api/recipes?_app_id=1f0647bd&_app_key=INSERT KEY'
x=input('input enter type of food')
p='&q='+x;
y='&maxResult=50';
t=search_base+p+y;
#end of url creation

r= requests.get(t)
x=r.json()

client = MongoClient('localhost:27017')
db = client.myFirstDb #myFirstDb is the name of database

db.myFirstDb11.insert(x)


