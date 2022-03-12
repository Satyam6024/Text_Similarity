
from flask import Flask,redirect,render_template,request
from flask import Flask
import pickle
model=pickle.load(open("E:\\python project\\text similarity\\sd.pkl","rb"))
s=model.cs(["i am good boy"], ["i am not a good boy"])


app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        var1=request.form["teacher"]
        var2=request.form["student"]
        s=copy([var1],[var2])
        return render_template('accuracy.html',var3=[var1,var2,s])
    return render_template('home.html')

@app.route('/accuracy',methods=["GET","POST"])
def accuracy():
    return render_template('accuracy.html')

def copy(s1,s2):
    global model
    m=model.cs(s1,s2)
    return m
if __name__ == '__main__':
   app.run(debug = True)