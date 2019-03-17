from db import user_collection
from bson import ObjectId
def add_user(username, password):
    new_user = {
        "username":username,
        "password":password,
    }
    user_collection.insert_one(new_user)

def get(query): #filter, limit = 5, skip = 10
    user_list = user_collection.find(query) #many
    return user_list

def get_by_id(id):
    u = user_collection.find_one( { "_id": ObjectId(id)} )
    return u    
def get_by_username(username):
    u = user_collection.find_one( { "username": username} )
    return u        
def delete_by_id(id):
    user_collection.delete_one({ "_id": ObjectId(id) })

def update_by_id(id, username, password):
    user_collection.find_one_and_update({ "_id":ObjectId(id) })    
    user_collection.find_one_and_update( {"$set": { "username": username }, "$set": { "password": password }})   

if __name__ == "__main__": 
    add_user("Dung1","12345")
    add_user("Dung2","12346")
    add_user("Dung3","12347")
    add_user("Dung4","12348")
    add_user("Dung5","12349")
