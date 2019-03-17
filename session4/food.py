from db import food_collection
from bson import ObjectId
def add_food(name, price):
    new_food = {
        "name":name,
        "price":price,
    }
    food_collection.insert_one(new_food)

def get(query): #filter, limit = 5, skip = 10
    food_list = food_collection.find(query) #many
    return food_list

def get_by_id(id):
    f = food_collection.find_one( { "_id": ObjectId(id)} )
    return f    
def delete_by_id(id):
    food_collection.delete_one({ "_id": ObjectId(id) })

def update_by_id(id, name, price):
    food_collection.find_one_and_update({ "_id":ObjectId(id) })    
    food_collection.find_one_and_update( {"$set": { "name": name }, "$set": { "price": price }})     
if __name__ == "__main__": 
    
    update_by_id("5c8124e38d1a22198462314b","Banh cuon",10000)
    print(*get({}),sep="\n")
    # delete_by_id("5c8128478d1a22209cd58afd")
    # f = get_by_id("5c8128478d1a22209cd58afd")
    # if f != None: #found
    #     print(f["name"])
    # else:
    #     print("Not found !")    
    # # for food in get({ "_id": ObjectId("5c8128478d1a22209cd58afd")}):
    #     # print(food)

