from flask import Flask, render_template, jsonify, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "SOME_KEY"


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/text")
def text():
    return render_template("Info.txt"), 200, {"Content-Type": "text/plain"}


@app.route("/xml")
def xml():
    return "<h1>This is xml</h1>", \
           200, \
           {"Content-Type": "application/xml"}


@app.route("/json")
def json():
    return jsonify({"Name": "Mike", "Age: ": 32})


@app.route("/redirect")
def redirect_page():
    return redirect(url_for("text"))


@app.route("/cookie")
def cookie_demo():
    result = redirect(url_for("home"))
    result.set_cookie("message", "Nice to see you!")
    return result


@app.route("/error")
def error_demo():
    return "Bad request", 500


if __name__ == "__main__":
    app.run(debug=True)
