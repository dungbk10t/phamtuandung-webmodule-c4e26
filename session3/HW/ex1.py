from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect.
client = MongoClient(uri)
# 2. Get database.
db = client.c4e
# 3. Get collectiion.
posts_collection = db["posts"]
customers_collection = db["customers"]

# 4. Creat a new document. 
# 5. InSert new doccumetn into collection.
# 6. Close connection.

def close():
    client.close()













