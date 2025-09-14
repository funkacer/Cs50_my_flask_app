# pip install -r requirements.txt
# mkdir templates
# flask run

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    #name = request.args["name"] # 400 error: Bad Request The browser (or proxy) sent a request that this server could not understand.
    #name = request.args.get("name", "world")
    #return "hello, world"
    #return render_template("index.html", placeholder = name)
    return render_template("index.html")


@app.route("/greet", methods = ["GET", "POST"])
def greet():
    #name = request.args.get("name", "world") # pro GET
    name = request.form.get("name", "world") # pro POST
    # 500 error: Internal Server Error The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
    return render_template("greet.html", name = name)