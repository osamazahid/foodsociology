import requests
import numpy as np
import math
import string
import json
import pymongo
import urllib2
import time
from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity


start_time = time.time()



##connection=MongoClient("ds1xxxxx.mlab.com", xxxxx)
##db1 = connection["database name"]
##db1.authenticate("usename", "password")
##collection=db1["collection name"]

try:
   
    client = MongoClient('localhost:27017')

    db = client.myfyp

except pymongo.error.ConnectionFailure,e:
    print "could not connect to MongoDB" %s %e






query=[db.pakistani.find_one(),db.indian.find_one(),db.chinese.find_one(),db.mongolian.find_one(),db.hong.find_one(),db.asian.find_one(),db.korean.find_one(),db.taiwanese.find_one(),db.japanese.find_one(),db.cantonese.find_one()
       ,db.afghani.find_one(),db.argentinian.find_one(),db.aruba.find_one(),db.canadian.find_one(),db.italianamerican.find_one(),db.louisiana.find_one(),db.cajun.find_one(),db.american.find_one(),db.basque.find_one()
       ,db.french.find_one(),db.dutch.find_one(),db.arab.find_one(),db.turkish.find_one(),db.welsh.find_one(),db.latinamerican.find_one(),db.mexican.find_one(),db.cuban.find_one(),db.colombian.find_one(),db.aztec.find_one(),db.caribbean.find_one()
       ,db.peruvian.find_one(),db.jamaican.find_one(),db.chilean.find_one(),db.brazilia.find_one(),db.spanish.find_one(),db.portuguese.find_one(),db.italian.find_one(),db.swiss.find_one(),db.saintlucian.find_one(),db.sicilian.find_one(),db.belgian.find_one(),db.oceanic.find_one()
       ,db.corni.find_one(),db.maltese.find_one(),db.irish.find_one(),db.polish.find_one(),db.german.find_one(),db.russian.find_one(),db.croatian.find_one(),db.hungarian.find_one(),db.ukrainian.find_one(),db.austrian.find_one(),db.danish.find_one()
       ,db.british.find_one(),db.english.find_one(),db.icelandic.find_one(),db.australian.find_one()
       ,db.scottish.find_one(),db.norwegian.find_one(),db.finnish.find_one(),db.mediterranean.find_one(),db.greek.find_one(),db.romanian.find_one(),db.bulgarian.find_one(),db.armer.find_one(),db.lebanese.find_one(),db.syrian.find_one(),db.iranian.find_one()
       ,db.moroccan.find_one(),db.african.find_one(),db.israeli.find_one(),db.egyptian.find_one(),db.tunisian.find_one(),db.ethiopian.find_one(),db.srilankan.find_one(),db.punjabi.find_one(),db.bengali.find_one(),db.indonesian.find_one()
       ,db.lao.find_one(),db.phillippine.find_one(),db.malaysian.find_one(),db.cambodian.find_one(),db.vietnamese.find_one(),db.thai.find_one(),db.bosnian.find_one(),db.cyprus.find_one(),db.estonian.find_one(),db.jordan.find_one()]
query1=['pakistani','indian','chinese','mongolian','hong','asian','korean','taiwanese','japanese','cantonese','afghani','argentinian','aruba','canadian','italian-american','louisiana','cajun','american','basque','french','dutch','arab','turkish','welsh','latin-american','mexican','cuban','colombean','aztec','caribbean','peruvian','jamaican'
        ,'chilean','brazilia','spanish','portugese','italian','swiss','saint-lucian','sicilian','belgian','oceanic','corni','maltese','irish','polish','german','russian','croatian','hungerian','ukrainian','austrian','danish','british','english','icelandic','australian'
        ,'scottish','norwegian','finnish','mediterranean','greek','romanian','bulgarian','armer','lebanese','syrian','iranian','moroccan','african','israeli','egyptian','tunisian','ethiopian','srilankan','punjabi','bengali','indonesian'
        ,'lao','phillippine','malaysian','cambodian','vietnamese','thai','bosnian','cyprus','estonian','jordan']

print "select from folloing and make sure spell same",query1

print '\n'

inp=input('Enter Country Name    ')



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
##print quer

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
##print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
for doc in quer:
    ##print 'The doc is "' + doc + '"'
    tf_vector = [tf(word, doc) for word in vocabulary]
    tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
    ##print 'The tf vector for Document %d is [%s]' % ((mydoclist.index(doc)+1), tf_vector_string)
    doc_term_matrix.append(tf_vector)
    
    # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
    # try it!  type(mydoclist.index(doc) + 1)


def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]

doc_term_matrix_l2 = []
for vec in doc_term_matrix:
    doc_term_matrix_l2.append(l2_normalizer(vec))

##print '\nA document term matrix with row-wise L2 norms of 1:'
##print np.matrix(doc_term_matrix_l2)



def numDocsContaining(word, doclist):
    doccount = 0
    for doc in doclist:
        if freq(word, doc) > 0:
            doccount +=1
    return doccount 
    

def idf(word, doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word, doclist)
    return np.log(n_samples / 1+df)

my_idf_vector = [idf(word, mydoclist) for word in vocabulary]

##print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
##print 'The inverse document frequency vector is [' + ', '.join(format(freq, 'f') for freq in my_idf_vector) + ']'
##



def build_idf_matrix(idf_vector):
    idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(idf_mat, idf_vector)
    return idf_mat

my_idf_matrix = build_idf_matrix(my_idf_vector)


doc_term_matrix_tfidf = []

#performing tf-idf matrix multiplication
for tf_vector in doc_term_matrix:
    doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

#normalizing
doc_term_matrix_tfidf_l2 = []
for tf_vector in doc_term_matrix_tfidf:
    doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))



p=[]
p1=[]
def cosine_similarity(v1,v2): ##cosine similarity function
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx =sumxx+x*x
        sumyy = sumyy+y*y
        sumxy = sumxy+x*y
    return (sumxy/math.sqrt(sumxx*sumyy))*100




#getting input wala document out

for qw in range(len(query1)):
    if (inp==query1[qw]):
	    index=qw
	    
t=doc_term_matrix_tfidf_l2.pop(index)
z=query1.pop(index)
no=0

#calling cosine similarity function
for n in doc_term_matrix_tfidf_l2:
    w=query1[no]
    s=cosine_similarity(t,n)
    #s=z+'-'+w+'==>'+str(s)
    #s1=z+'-'+w
    p1.append(w)
    p.append(s)
    no=no+1


    
for io in range(len(p)):
    x1=p.pop()
    x2=p1.pop()
    x1=str(x1)
    x2=str(x2)
    dic={"similarity": x1,'food': x2}
    json=json.dumps(dic)
    print dic
    "putting data in database"
    #db1.tb.insert(dic)
    #collection.insert(dic)
    #print "data added"
    "here ends"
##    print x1
##    print x2
##    print '\n'
print dic
"printing data rom database"
"use it in other file"
##for doc in db1.pakistaniresults.find():
##    print doc
##    print '\n' 
"here ends the data printing"
print("--- %s seconds ---" % (time.time() - start_time))

