from flask import Flask, render_template, request
app = Flask(__name__)

items = [
  {
    "model":"WINNER 150cc",
    "daily_fee": 45490000,
    "image":"https://hondaxemay.com.vn/wp-content/uploads/2018/12/165x205_xe-1_165x205_acf_cropped.png",
    "year":2019,
  },
  {
    "model":"EXCITER 150",
    "daily_fee": 47990000,
    "image":"https://yamaha-motor.com.vn/wp/wp-content/uploads/2018/07/500x400-8.png",
    "year":2019,
  },
]

@app.route('/')
def menu():
    return render_template("menu.html", item_list = items, user = "DUNG")

@app.route("/new_bike", methods = ['GET','POST'])
def new_bike():
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
          "year":y
        }
        items.append(new_item)
        return "DA THEM THANH CONG"  

if __name__ == '__main__':
  app.run(debug=True)