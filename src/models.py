# All the models used in the website

class Post(db.Model):
	id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
	board = db.Column(db.String(1), nullable=False)
	content = db.Column(db.String(200000))

	def __str__(self):
		return f"Post <#{self.id} in /{self.board}>"

	def __repr__(self):
		return __str__()
