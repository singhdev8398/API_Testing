from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/math",methods=["POST"])
def test():
    if (request.method=="POST"):
         a=request.json["num1"]
         b=request.json["num2"]
         sum=a+b
    return jsonify(str(sum))


@app.route("/math/dev",methods=["POST"])
def test1():
    if (request.method=="POST"):
         a=request.json["num3"]
         b=request.json["num4"]
         sum=a+b
    return jsonify(str(sum))


@app.route("/math/dev/d",methods=["POST"])
def test2():
    if (request.method=="POST"):
         a=request.json["num5"]
         b=request.json["num6"]
         sum=a+b
    return jsonify(str(sum))


@app.route("/math/dev/d/singh",methods=["POST"])
def test3():
    if (request.method=="POST"):
         a=request.json["num7"]
         b=request.json["num8"]
         sum=a+b
    return jsonify(str(sum))


if __name__=="__main__":
      app.run(debug=True,port=5000)

