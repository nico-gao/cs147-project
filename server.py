from flask import Flask 
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    print(request.args.get("var"))
    print(request.args.get("var2"))
    return "We received value: " + str(request.args.get("var")) + " " + str(request.args.get("var2"))