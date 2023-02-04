from flask import Flask
from calc_func.addition import Addition
from calc_func.subtration import Subtration
from calc_func.multiplication import Multiplication
from calc_func.division import Division

app = Flask(__name__)
addition = Addition()
subtration = Subtration()
multiplication = Multiplication()
division = Division()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add/<a>/<b>')
def add2num(a,b):
    sum=addition.add2n(int(a),int(b))
    return 'Addition of '+a+' and '+b+ ' is '+str(sum)

@app.route('/add/<a>/<b>/<c>')
def add3num(a,b,c):
    sum=addition.add3n(int(a),int(b),int(c))
    return 'Addition of '+a+' and '+b+ ' and ' +c+' is '+str(sum)

@app.route('/sub/<a>/<b>')
def sub2num(a,b):
    sub=subtration.sub2n(int(a),int(b))
    return 'Subtration of '+a+' and '+b+ ' is '+str(sub)

@app.route('/sub/<a>/<b>/<c>')
def sub3num(a,b,c):
    sub=subtration.sub3n(int(a),int(b),int(c))
    return 'Subtration of '+a+' and '+b+ ' and '+c+' is '+str(sub)

@app.route('/mul/<a>/<b>')
def mul2num(a,b):
    mul=multiplication.mul2n(int(a),int(b))
    return 'Multiplication of '+a+' and '+b+ ' is '+str(mul)

@app.route('/mul/<a>/<b>/<c>')
def mul3num(a,b,c):
    mul=multiplication.mul3n(int(a),int(b),int(c))
    return 'Multiplication of '+a+' and '+b+ ' and '+c+' is '+str(mul)

@app.route('/div/<a>/<b>')
def div2num(a,b):
    div=division.div2n(int(a),int(b))
    return 'Division of '+a+' and '+b+ ' is '+str(div)

app.run()

