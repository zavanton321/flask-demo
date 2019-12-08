from datetime import datetime

from flask import Flask, render_template, session, g
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "SOME_KEY"


@app.before_request
def before():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    g.when = datetime.now().strftime("%H:%M:%S")


@app.route("/")
def home():
    return render_template("main.html", count=session["count"], when=g.when)


@app.route("/other")
def other():
    return render_template("other.html", count=session["count"], when=g.when)


if __name__ == "__main__":
    app.run(debug=True)
