from flask import Flask, render_template, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "SOME_KEY"


@app.route("/")
def home():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template("main.html", count=session["count"])


if __name__ == "__main__":
    app.run(debug=True)
