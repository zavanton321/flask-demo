import imghdr
import os

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config["SECRET_KEY"] = "SOME_KEY"
bootstrap = Bootstrap(app)


class RegistrationForm(Form):
    first_name = StringField("First name: ", validators=[DataRequired(), Length(1, 10)])
    last_name = StringField("Last name: ", validators=[DataRequired(), Length(1, 10)])
    age = IntegerField("Age: ", validators=[DataRequired()])
    image_file = FileField("Upload your avatar")
    submit = SubmitField("Submit")

    def validate_image_file(self, field):
        if imghdr.what(field.data) != "jpeg":
            raise ValidationError("The image file is invalid!")


@app.route("/", methods=["GET", "POST"])
def index():
    first_name = None
    last_name = None
    age = 0
    avatar = None

    form = RegistrationForm()

    if form.validate_on_submit():
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        age = request.form["age"]

        uploaded = form.image_file.data
        avatar = "uploads/" + uploaded.filename
        uploaded.save(os.path.join(app.static_folder, avatar))

    return render_template("index.html",
                           first_name=first_name,
                           last_name=last_name,
                           age=age,
                           avatar=avatar,
                           form=form)


@app.errorhandler(404)
def error404(error):
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
