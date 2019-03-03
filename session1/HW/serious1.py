from flask import Flask,redirect
app = Flask(__name__)
@app.route('/bmi/<int:weight>/<int:height>')

def calbmi(weight,height):
    height = height / 100
    BMI = weight / (height*height)
    if BMI < 16:
        return "BMI = %.2f: Severely underweight"%BMI
    elif BMI < 18.5:
        return "BMI = %.2f: Underweight"%BMI
    elif BMI < 25: 
        return "BMI = %.2f: Normal"%BMI
    elif BMI < 30: 
        return "BMI = %.2f: Overweight"%BMI
    else: 
        return "BMI = %.2f: Obese"%BMI

if __name__ == '__main__':
  app.run(debug=True)