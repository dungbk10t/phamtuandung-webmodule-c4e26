from flask import Flask,render_template,request

app = Flask(__name__)

bikes = [
    {
        "model":"Honda",
        "daily_fee": 10000,
        "image":"https://hondaoto.com.vn/static/uploads/editor/CV1.JPG",
        "year":2013,
    },
    {
        "model":"Yamaha",
        "daily_fee": 15000,
        "image":"https://hondaoto.com.vn/static/uploads/editor/CV1.JPG",
        "year":2015,
    },
]   

users = "Dung"
@app.route("/") #ALL => List/Master
def menu():
    return render_template("menu.html", item_list=bikes, user="Dung")

@app.route("/new_bike", methods=["GET","POST"])
def add_food():
    if request.method == "GET":
        return render_template("bike_form.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        d = form["daily_fee"]
        i = form["image"]
        y = form["year"]
        new_item = {
            "model":m,
            "daily_fee":d,
            "image":i,
            "year":y,
        }
        bikes.append(new_item)
        return "ADD thanh cong" 

if __name__ == '__main__':
  app.run(debug=True)