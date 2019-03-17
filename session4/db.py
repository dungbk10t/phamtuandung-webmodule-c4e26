from pymongo import MongoClient

uri = "mongodb+srv://admin:admin1@cluster0-tgxio.mongodb.net/test?retryWrites=true"

# 1. Connect.
client = MongoClient(uri)
# 2. Get database.
db = client.test

# 3. Get collectiion.
food_collection = db["food"]

# # 4. Creat a new document. 
# new_food = {
#     "name": "Com rang",
#     "price": 30000,
# }#document

# # 5. InSert new doccumetn into collection.
# food_collection.insert_one(new_food)

# 6. Close connection.
def close():
    client.close()













