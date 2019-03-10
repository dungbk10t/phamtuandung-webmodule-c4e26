from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect.
client = MongoClient(uri)
# 2. Get database.
db = client.c4e
rivers_collection = db["river"]

def close():
    client.close()
