import os

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
dbf = "sqlite:///dela.db"
app.config["SQLALCHEMY_DATABASE_URI"] = dbf
app.config["SECRET_KEY"] = 'you-will-never-guess'
db = SQLAlchemy(app)

class Post(db.Model):
	id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
	board = db.Column(db.String(2), nullable=False)
	content = db.Column(db.String(200000))

	def __str__(self):
		return f"Post <#{self.id} in /{self.board}/>"

	def __repr__(self):
		return __str__()


@app.route('/')
def home():
	return render_template("home.html")

@app.route('/<board>/', methods=['POST', 'GET'])
def board(board):
	if request.method == 'POST':
		post_content = request.form["content"]
		post_board = board
		new_post = Post(content=post_content, board=post_board)
		db.session.add(new_post)
		db.session.commit()
		return redirect('/g/')
	else:
		posts = Post.query.filter_by(board=board).all()
		return render_template("board.html", board=board, posts=posts)

if __name__ == '__main__':
	app.run(debug=True)