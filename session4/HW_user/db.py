from pymongo import MongoClient

uri = "mongodb+srv://admin:admin1@cluster0-tgxio.mongodb.net/test?retryWrites=true"

# 1. Connect.
client = MongoClient(uri)
# 2. Get database.
db = client.test

# 3. Get collectiion.
user_collection = db["user"]

# 6. Close connection.
def close():
    client.close()













