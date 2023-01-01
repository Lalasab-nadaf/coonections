import pymongo
client = pymongo.MongoClient("mongodb+srv://lalsabnadaf143:Armanjaan@786@cluster1.nz37pbt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)