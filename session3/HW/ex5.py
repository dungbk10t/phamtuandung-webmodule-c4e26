from ex4 import rivers_collection
river_list = rivers_collection.find(
        {
            "continent":"Africa",
        }
    )    #lazy loading 

print(river_list)
for i in river_list:
    print(i["name"])
    print(i["continent"])
    print(i["length"])   
    print('=================')