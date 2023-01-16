from flask import Flask, render_template, request, redirect, url_for

# from flask_sqlalchemy import SQLAlchemy
from food_data import NutritionalAPI
from usda import USDA

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


# class Todo(db.Model):
# id = db.Column(db.Integer, primary_key=True)
# title = db.Column(db.String(100))
# complete = db.Column(db.Boolean)

# class FoodData(db.Model):
# id = db.Column(db.Integer, primary_key=True)


# Creating tables
# with app.app_context():
# db.create_all()


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html")


@app.route("/data/", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return (
            f"The URL /data is accessed directly. Try going to '/form' to submit form"
        )
    if request.method == "POST":
        form_data = NutritionalAPI(request.form["UPC Code"])
        return render_template("data.html", form_data=form_data)


@app.route("/usda", methods=["GET"])
def usda():
    return render_template("usda.html")


@app.route("/usda_data/", methods=["POST", "GET"])
def usda_data():
    if request.method == "GET":
        return (
            f"The URL /data is accessed directly. Try going to '/form' to submit form"
        )
    if request.method == "POST":
        form_data = USDA(request.form["item"], request.form["pages"]).get_data()
        return render_template("usda_data.html", form_data=form_data)


if __name__ == "__main__":
    app.run(port=5000)
