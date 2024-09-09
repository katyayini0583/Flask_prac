from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/ping", methods=["GET"])
def pinger():
    return {"MESSAGE" : "Hi, I am Pinging...!!!!!"}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
