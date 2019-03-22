from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#Use template
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height = height/100
    BMI = round(weight/(height*height),2)
    return render_template('bmi.html',BMI = BMI)

#No use template
@app.route('/bmi1/<int:weight>/<int:height>')
def bmi1(weight,height):
    height = height/100
    BMI = round(weight/(height*height),2)
    print("Your BMI: ",BMI)
    if BMI < 16:
        notify = "You are severely underweight"
    elif 16 <= BMI <=  18.5:
        notify = "You are underweight"
    elif 18.5 < BMI <= 25:
        notify = "You are normal"
    elif 25 < BMI <= 30:
        notify = "You are overweight"
    elif BMI > 30:
        notify = "You are obese"
    return "Your BMI: " + str(BMI) + " ."+ notify

if __name__ == '__main__':
  app.run(debug=True)
 