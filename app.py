from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "welcome to my youtube channel"

if __name__=="__main__":
      app.run(debug=True,port=3000)