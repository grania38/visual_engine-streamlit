import pymongo
from pymongo import MongoClient
import numpy as np
from sklearn.cluster import KMeans

#MongoDB

client=MongoClient('mongodb://localhost:27017/imageDB')
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")


db=client.imageDB
collection=db.images

path='C:/cbir2/eh_descriptors'


table=[]
n=10
for k in range(1,n+1,1):
	print("reading features" + str(k))
	with open(path+ '/eh'+str(k)+'.txt','r') as f:
		#x = mycol.insert_many(f)
		lines=f.readlines()

	for i in lines:
		table.append(i.split())
	edge=np.array(table)

print("finished reading")
#Kmeans clustering
Kmeans = KMeans(n_clusters=200).fit(edge)
Clusters = Kmeans.predict(edge)
centroids = Kmeans.cluster_centers_
print("finished clustering")
for k in range(0,100000):
    cluster=str(Clusters[k])
    
    line_DB={"index":k,"edge_value":table[k],"cluster":cluster}
    collection.insert_one(line_DB)
    #print(str(k) + "is added")


    
