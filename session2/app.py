from flask import Flask,render_template,request

app = Flask(__name__)

items = [
    {
        "name":"Com rang",
        "price": 25000,
    },
    {
        "name":"Pho bo",
        "price": 25000,
    },
    {
        "name":"Xoi xeo",
        "price": 10000,
    },
] 

users = "Dung"
# @app.route("/") #ALL => List/Master
# def menu():
#     return render_template("menu.html", item_list=items, user="Dung")
# @app.route("/food/<int:i>") # => Deltai
# def food(i):
#     f = items[i]
#     return render_template("food_detail.html", item=f, user="Master")

@app.route("/add_food", methods=["GET","POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        new_item = {
            "name":n,
            "price":p,
        }
        items.append(new_item)
        return "ADD: " + n + " " + str(p)

if __name__ == '__main__':
  app.run(debug=True)