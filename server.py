from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape
import opensesame
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/open", methods=["GET", "POST"])
def open_door():
    if request.method == "POST":
        # Open the garage door
        opensesame.open_door()
    return redirect("/")

@app.route("/close", methods=["GET", "POST"])
def close_door():
    if request.method == "POST":
        # Close the garage door
        opensesame.close_door()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)