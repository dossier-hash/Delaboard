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
	ok_boards = {
		'tg': 'General talking space for tech cucks',
		'ag' : 'General talking space for fat weeaboos',
		'g' : 'General talking space for all delars',
		'p' : 'Programming talk and shit',
		'h' : '/''Tis hentai',
		'f' : 'Talk about good cuisine',
		'l' : 'LINUX ONLY; FUCK YOU',
		'yy' : 'Talk about that gross yaoi/yuri shit',
		'o' : 'No restrictions. Talk about your shit opinions'
	}

	if request.method == 'POST':
		post_content = request.form["content"]
		post_board = board
		new_post = Post(content=post_content, board=post_board)
		db.session.add(new_post)
		db.session.commit()
		return redirect('/g/')
	else:
		if board in ok_boards.keys():
			posts = Post.query.filter_by(board=board).all()
			return render_template("board.html", board=board, 
				posts=posts, description=ok_boards[board])
		else:
			return redirect('/')

@app.route('/<board>/post/<int:postid>', methods=['POST', 'GET'])
def post(postid):
	if request.method == 'POST':
		pass
	else:
		pass

if __name__ == '__main__':
	app.run(debug=True)