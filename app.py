from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from food_data import NutritionalAPI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Creating tables
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    chips = NutritionalAPI("014100053293")

    return f'Name: {chips.data.brand_name}'


if __name__ == '__main__':
    app.run()