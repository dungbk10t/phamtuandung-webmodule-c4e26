from ex1 import customers_collection
import matplotlib.pyplot as plt


customers_list = customers_collection.find()
e = 0
w = 0
a = 0
for c in customers_list:
    if (c["ref"] == "events"):
        e+=1
    elif(c["ref"] == "wom"):
        w+=1
    elif(c["ref"] == "ads"):   
        a+=1
s = e + w + a
datas = [e/s,w/s,a/s]
label_data = ['events','wom','ads']
color_data = ["#0d13c4","#c40d0d","#f9e902"]
plt.pie(datas, labels=label_data, colors=color_data,shadow=True, autopct='%1.1f%%',radius=1.5)
plt.axis("equal")
plt.show()
    