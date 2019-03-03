from flask import Flask,redirect
app = Flask(__name__)

@app.route('/about-me')
def about():
  myseft = {
    "Name": "Dung",
    "Age": "21",
    "Hobbies": "Travel",
    "Work": "Student",
  }
  return str(myseft)
@app.route('/')
def school():
  return redirect("https://techkids.vn/", code=302)
if __name__ == '__main__':
  app.run(debug=True)