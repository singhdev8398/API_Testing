from flask import Flask,request,jsonify
app=Flask(__name__)


@app.route("/")
def home_page ():
   return "<h2>This is my first flask</h2>"

@app.route("/sunny",methods=["POST"])
def operation():
    if (request.method=="POST"):
        first_name=request.json["firstname"]
        last_name=request.json["lastname"]
        result=f"myy full name is : {first_name+last_name}"
    return jsonify(result)

@app.route("/math",methods=["POST"])
def add_number():
    if (request.method=="POSt"):
         a=request.json(["fistnumber"])
         b=request.json(["secondnumber"])
         sum=a+b
    return jsonify(sum)


if __name__=="__main__":
     app.run(host="0.0.0.0",port=6000)
