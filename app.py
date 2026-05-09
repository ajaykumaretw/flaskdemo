# Rounting in Flask
from flask import Flask,render_template,request,url_for,redirect,jsonify
import pandas as pd 
import webbrowser
app=Flask(__name__)

@app.route("/",methods=["GET"])# For Home Page
def welcome():
  return "Hi I am Ajay Kumar: I am Senior ML Enginner"

@app.route("/contactUs",methods=["GET"])# For Home Page
def contactUs():
  return "9650543959"

@app.route("/index/myindex",methods=["GET"])# For Home Page
def index():
  return "Index Page"


@app.route("/browse",methods=["Get"])
def browse():
  webbrowser.open("https://abc.com/browse")

@app.route("/api/calculation",methods=["POST"])
def CalculateSum():
  print(request.args)
  x = request.args.get("x")
  y = request.args.get("y")
  print(x)
  print(y)
  data =request.get_json()
  a=float(dict(data)["a"])
  b=float(dict(data)["b"])
  c=a+b
  mylist=[
    {'Name':'Ajay Kumar','Age':21,"deparement":"it"},
    {'Name':'Alok','Age':29,"deparement":"finance"},
    {'Name':'Rakesh M','Age':30,"deparement":"development"}   
  
  ]
  dt =pd.read_csv("sales_data_sample.csv",encoding="ISO-8859-1")
  return dt.to_html()
def cal(mylist):
 return eval("*".join([str(val) for val in mylist]))

@app.route("/result/<string:Score>")
def getResult(Score):
  Score=Score.split(',')
  return f"Score is:"+ str(cal(Score))


@app.route("/success/<int:Score>")
def success(Score):
  return f"You got success with Agerage marks have: {Score}"


@app.route("/fail/<int:Score>")
def fail(Score):
  return f"You got failed with Agerage marks have {Score}"

@app.route("/form", methods=["GET", "POST"])
def form():
     result=''
     avg_marks=0
     if request.method == "POST":
         maths = int(request.form['maths'])
         science = int(request.form['science'])
         history = int(request.form['history'])
         avg_marks = (maths + science + history) / 3
         #return render_template("form.html",avg_marks=avg_marks)
    
         if avg_marks>50:
           result="success"
         else:
           result="fail"
         url =url_for(result,Score=int(avg_marks))
         return redirect(url)
     elif request.method.upper()=="GET":
        return render_template('form.html')
if __name__== "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
