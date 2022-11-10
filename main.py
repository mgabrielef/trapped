from flask import Flask, render_template, request
import random


app = Flask(__name__, template_folder='templates', static_folder='static')

a = 0
b = 100
randomNumber = random.randint(1, 99)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
  d = request.form['number']
  try:
    number = int(d)
  except:
    if type(d) != int:
      msg = "Not a number. You should type a number between 0 and 100"
      return render_template("tryagain.html", value=msg)

  while(True):
    global a
    global b
    global randomNumber
    if number == randomNumber:
      a = 0
      b = 100
      randomNumber = random.randint(1, 99)
      return render_template("result.html")
    if number != randomNumber:
      if number not in range(0, 100):
        msg = "OUT OF RANGE! TRY A NUMBER BETWEEN 0 AND 100."
        number = int(request.form['number'])
        return render_template("tryagain.html", value=msg)
      elif number > randomNumber:
        if number in range(a, b):
          b = number
          msg = " BETWEEN "
          msg2 = " AND "
          number = int(request.form['number'])
          return render_template("tryagain.html", value=msg, value2=msg2, a=a, b=b)
        else:
          msg = "OUT OF RANGE! TRY A NUMBER BETWEEN "
          msg2 = " AND "
          number = int(request.form['number'])
          return render_template("tryagain.html", value=msg, value2=msg2, a=a, b=b)
      elif number < randomNumber:
        if number in range(a, b):
          a = number
          msg = "BETWEEN "
          msg2 = " AND "
          number = int(request.form['number'])
          return render_template("tryagain.html", value=msg, value2=msg2, a=a, b=b)
        else:
          msg = "OUT OF RANGE! TRY A NUMBER BETWEEN "
          msg2 = " AND "
          number = int(request.form['number'])
          return render_template("tryagain.html", value=msg, value2=msg2, a=a, b=b)
      return render_template("tryagain.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
