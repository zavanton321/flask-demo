import imghdr
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SubmitField, FileField, ValidationError

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY_KEY"
bootstrap = Bootstrap(app)


class UploadForm(Form):
    image_file = FileField("Image File")
    submit = SubmitField("Submit")

    def validate_image_file(self, field):
        if field.data.filename[-4:].lower() != ".jpg":
            raise ValidationError("Invalid file extension!")
        if imghdr.what(field.data) != "jpeg":
            raise ValidationError("Invalid image format!")


@app.route("/", methods=["GET", "POST"])
def index():
    image = None
    form = UploadForm()

    if form.validate_on_submit():
        image = "uploads/" + form.image_file.data.filename
        form.image_file.data.save(os.path.join(app.static_folder, image))
    return render_template("index.html", form=form, image=image)


if __name__ == "__main__":
    app.run(debug=True)
