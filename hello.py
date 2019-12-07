from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField

from wtforms.validators import Length, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY_KEY"
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField("Name: ", validators=[DataRequired(), Length(1, 16)])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("index.html", name=name, form=form)


if __name__ == "__main__":
    app.run(debug=True)
