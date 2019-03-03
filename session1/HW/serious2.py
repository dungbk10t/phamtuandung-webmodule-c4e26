from flask import Flask
app = Flask(__name__)

@app.route("/user/<name>")

def username(name):
    Users = {
        "dung": {
                "Name":"Pham Tuan Dung", 
                "Age": 21,
                "sex": "Male",
                "Hobbies":"None",
                },
        "long": {
                "Name":"Nguyen Vu Long",
                "Age": 20,
                "Sex":"Male",
                "Hobbies":"Anime",
                },
        "le":   {
                "Name":"Ton Tieu Le",
                "Age": 19,
                "Sex":"female",
                "Hobbies":"Ngon Tinh",
                },
    } 
    if name not in Users:
        return "User not found"
    else:
        return str(Users[name])

if __name__ == '__main__':
  app.run(debug=True)