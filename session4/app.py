from flask import Flask,render_template,request
import food
app = Flask(__name__)

@app.route("/food_list") #ALL => List/Master
def food_list():
    #B1 GET ALL FOOD 1.Funton ? 2.Write funtion ?
    all_food = food.get({}) #lấy hết.
    #B2: render: ALL FOOD + html

    #B3: Return

    return render_template("food_list.html", f_list=all_food)
@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return render_template("food_detail.html",food = f,user="Dung")
    # return f["name"]
@app.route("/add_food",methods = ["GET","POST"])
def add_food():
  if request.method == "GET":
    return render_template("food_form.html")
  elif request.method == "POST":
    form = request.form
    n = form["name"]
    p = form["price"]
    food.add_food(n,p) 
    return "Da them thanh cong"

if __name__ == '__main__':
  app.run(debug=True)