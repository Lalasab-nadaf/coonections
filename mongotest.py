import pymongo
import urllib
client = pymongo.MongoClient("mongodb+srv://lalsabnadaf143:Armanjaan@cluster1.nz37pbt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"lalsab",
    "surname":"nadaf",
    "email":"lalsab@gmail.com"
}

db1 = client['mongodbtest']
coll=db1['test']
coll.insert_one(d)