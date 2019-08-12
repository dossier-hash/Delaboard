import os

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy 

dbf = "sqlite:///dela.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbf
db = SQLAlchemy(app)

@app.route('/')
def home():
	return render_template("home.html")


if __name__ == '__main__':
	app.run(debug=True)