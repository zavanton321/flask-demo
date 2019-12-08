from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///info.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), index=True)

    def __repr__(self):
        return "<User {}>".format(self.name)


class NameForm(Form):
    name = StringField("Name: ", validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField("Register")


@app.route("/", methods=['GET', 'POST'])
def home():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        db.session.add(User(name=name))
        db.session.commit()
    return render_template("home.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)
