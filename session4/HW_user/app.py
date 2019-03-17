from flask import Flask,render_template,request
import user
app = Flask(__name__)

@app.route("/user_list") #ALL => List/Master
def user_list():
    #B1 GET ALL FOOD 1.Funton ? 2.Write funtion ?
    all_user = user.get({}) #lấy hết.
    #B2: render: ALL FOOD + html

    #B3: Return

    return render_template("user_list.html", u_list=all_user)
@app.route("/user/<id>")
def user_detail(id):
    u = user.get_by_id(id)
    return render_template("user_detail.html",user = u,user1="Dung")
    # return f["name"]
@app.route("/add_user",methods = ["GET","POST"])
def add_user():
  if request.method == "GET":
    return render_template("user_form.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["username"]
    user.add_user(u,p) 
    return "Da them thanh cong"
@app.route("/find_user", methods=["GET","POST"])
def find_user():
    if request.method=="GET":
        return render_template("find_user.html")
    elif request.method=="POST":
        form=request.form
        u=form["username"]
        check = user.get_by_username(u)
        if check != None:
          return "Tim thay  " + str(u)
        else:    
            return "Tai khoan khong ton tai !"
if __name__ == '__main__':
  app.run(debug=True)